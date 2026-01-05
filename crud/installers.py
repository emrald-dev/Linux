import subprocess
from pathlib import Path
from typing import Dict, List
from rich.console import Console
from rich.table import Table
import yaml
import typer

from .utils import cons, fs, copy_dir, copy_dir_contents

console = Console()
app = typer.Typer()


def flatten(groups: Dict[str, List[str]]) -> Dict[str, str]:
    """Flatten {group: [packages]} → {package: group}"""
    out = {}
    for group, pkgs in groups.items():
        for pkg in pkgs:
            out[pkg] = group
    return out


class DepsInstaller:
    def __init__(self, pacman: Dict, aur: Dict, inhouse: List[Dict], dry_run: bool = False):
        self.pacman = flatten(pacman)
        self.aur = flatten(aur)
        self.inhouse_list = inhouse
        self.failed = []
        self.skipped = []
        self.dry_run = dry_run

    def _exists(self, cmd: List[str]) -> bool:
        if self.dry_run:
            cons.print(f"[cyan]DRY-RUN[/] Checking existence: {' '.join(cmd)}")
            return True
        return subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0

    def _run_and_capture(self, cmd: List[str]):
        if self.dry_run:
            cons.print(f"[cyan]DRY-RUN[/] Would run: {' '.join(cmd)}")
            class DummyResult:
                returncode = 0
                stdout = "DRY-RUN: nothing executed"
            return DummyResult()
        return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    def install_pkg(self, manager: str, pkg: str):
        exists_cmd = ["pacman", "-Si", pkg] if manager == "pacman" else ["yay", "-Si", pkg]
        install_cmd = (
            ["sudo", "pacman", "-S", "--needed", "--noconfirm", pkg]
            if manager == "pacman"
            else ["yay", "-S", "--needed", "--noconfirm", pkg]
        )

        if not self._exists(exists_cmd):
            self.skipped.append(f"{manager}:{pkg}")
            cons.print(f"[yellow]SKIP[/] {pkg} (not found)")
            return

        result = self._run_and_capture(install_cmd)

        if result.returncode != 0:
            self.failed.append(f"{manager}:{pkg}")
            cons.print(f"[red]FAIL[/] {pkg}")
            if hasattr(result, "stdout"):
                cons.print(f"[yellow]{result.stdout.strip()}[/]")
            return

        if hasattr(result, "stdout") and ("is up to date" in result.stdout or "there is nothing to do" in result.stdout):
            cons.print(f"[cyan]OK[/] {pkg} (already installed)")
        else:
            cons.print(f"[green]OK[/] {pkg} installed")

    def install_inhouse(self, pkg: str):
        """Install a single in-house folder specified by `pkg`."""
        if not self.inhouse_list:
            self.skipped.append(f"inhouse:{pkg}")
            cons.print(f"[yellow]SKIP[/] In-house package {pkg} not defined")
            return

        item = next((i for i in self.inhouse_list if i["src"] == pkg), None)
        if not item:
            self.skipped.append(f"inhouse:{pkg}")
            cons.print(f"[yellow]SKIP[/] In-house package {pkg} not found in YAML")
            return

        src = fs.dev / item["src"]
        method = item.get("method", "dir")
        dest = fs.home if method == "contents" else fs.home / src.name

        try:
            if method == "contents":
                copy_dir_contents(src, dest)
            else:
                copy_dir(src, dest)
            cons.print(f"[green]OK[/] Installed in-house {pkg} → {dest}")
        except Exception as e:
            self.failed.append(f"inhouse:{pkg}")
            cons.print(f"[red]FAIL[/] {pkg} → {e}")

    def install_all(self):
        cons.print("[bold magenta]Installing official packages[/]")
        for pkg in self.pacman:
            self.install_pkg("pacman", pkg)

        cons.print("[bold magenta]\nInstalling AUR packages[/]")
        for pkg in self.aur:
            self.install_pkg("aur", pkg)

        cons.print("[bold magenta]\nInstalling in-house packages[/]")
        for item in self.inhouse_list:
            self.install_inhouse(item["src"])

    def summary(self):
        table = Table(title="\nInstallation Summary")
        table.add_column("Status", style="bold")
        table.add_column("Packages")

        if self.failed:
            table.add_row("Failed", "\n".join(self.failed))
        if self.skipped:
            table.add_row("Skipped", "\n".join(self.skipped))
        if not self.failed and not self.skipped:
            table.add_row("Success", "All packages installed")

        cons.print(table)


