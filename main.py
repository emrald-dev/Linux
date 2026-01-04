import typer
import yaml

from pathlib import Path

from crud import *

app = typer.Typer(help="My Linux CLI helper")

@app.command()
def ping():
    fs.ping_folders()

if __name__ == "__main__":
    app()

