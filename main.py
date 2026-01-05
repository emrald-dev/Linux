import yaml
import typer

from pathlib import Path

from crud import *

app = typer.Typer(help="My Linux CLI helper")


@app.command()
def theme(
    set: str | None = typer.Option(
        None,
        "--set",
        help="Theme name to apply (e.g. onedark, github)",
    ),
    get: bool = typer.Option(
        False,
        "--get",
        help="Print the currently active theme",
    ),
    update: bool = typer.Option(
        False,
        "--update",
        help="Update the system themes folder",
    ),
):
    if set:
        themes.set_theme(set)

    elif get:
        current_theme = themes.get_current_theme()
        if current_theme: 
            cons.print(current_theme)

    elif update:
        themes.update_themes()

    else:
        typer.echo("Nothing to do. Use --set or --get.")


@app.command()
def dots(
    update: bool = typer.Option(
        False,
        "--update",
        help="Update the system dotfiles",
    ),
):
    if update:
        dotfiles.update_dotfiles()


@app.command()
def install(
    deps: bool = typer.Option(
        False,
        "--deps",
        help="Install all dependencies (Arch official + AUR)."
    ),
):
    if deps:
        cons.print("Attempting to install dependencies, please wait.")

        # fs.deps should be something like:
        # {
        #   "pacman": { "base": ["git", "curl"], ... },
        #   "aur": { "custom": ["package1", "package2"], ... }
        # }

        # Load the YAML file
        with fs.deps.open("r", encoding="utf-8") as f:
            deps_data = yaml.safe_load(f) or {}

        pacman_pkgs = deps_data.get("pacman", {})
        aur_pkgs = deps_data.get("aur", {})

        depi = DepsInstaller(pacman=pacman_pkgs, aur=aur_pkgs, dry_run=False)
        depi.install_all()
        depi.summary()


@app.command()
def ping():
    fs.ping_folders()


@app.command()
def dev():
    cons.print("This feature will clone this project and create a workspace.")
    cons.print("Not implemented yet")


if __name__ == "__main__":
    app()

