import subprocess

from pathlib import Path

def copy_dir(src: Path, dst: Path) -> None:
    subprocess.run(
        ["mkdir", "-p", str(dst)],
        check=True,
    )
    subprocess.run(
        ["cp", "-a", str(src), str(dst)],
        check=True,
    )

def copy_dir_contents(src: Path, dst: Path) -> None:
    subprocess.run(
        ["mkdir", "-p", str(dst)],
        check=True,
    )
    subprocess.run(
        ["cp", "-a", "--", f"{src}/.", str(dst)],
        check=True,
    )
