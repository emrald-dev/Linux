import typer
import yaml

from pathlib import Path

app = typer.Typer(help="My Linux CLI helper")

from crud import *

@app.command()
def hello():
    cons.print("Helllo world")


if __name__ == "__main__":
    app()

