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
        help="Print the currently active theme",
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
def update():
    update_dotfiles()


@app.command()
def ping():
    fs.ping_folders()


@app.command()
def dev():
    cons.print("This feature will clone this project and create a workspace.")
    cons.print("Not implemented yet")


if __name__ == "__main__":
    app()

