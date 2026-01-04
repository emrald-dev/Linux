import typer
import yaml

from pathlib import Path

from crud import *

app = typer.Typer(help="My Linux CLI helper")

@app.command()
def ping():
    fs.ping_folders()

@app.command()
def dev():
    cons.print("This feature will clone this project and create a workspace.")
    cons.print("Not implemented yet")

if __name__ == "__main__":
    app()

