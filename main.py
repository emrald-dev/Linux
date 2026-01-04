import typer
import yaml

from pathlib import Path

app = typer.Typer(help="My Linux CLI helper")

from crud import *

@app.command()
def ping():
    logger.ping(f"(Home Folder) [cyan]{fs.home}[/cyan]")
    logger.ping(f"(Project Folder) [cyan]{fs.project}[/cyan]")
    logger.ping(f"(Deps Folder) [cyan]{fs.deps}[/cyan]")

if __name__ == "__main__":
    app()

