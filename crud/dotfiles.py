import subprocess

from pathlib import Path
from typing import Dict, List
from rich.console import Console
from rich.table import Table

from .utils import cons, fs, copy_dir_contents


class Dotfiles:
    def __init__(self):
        self.dev_dir = fs.dev / "dotfiles"
        self.sys_dir = fs.home

    def update_dotfiles(self):
        cons.print("Attempting dotfiles update, please wait.")
        try:
            copy_dir_contents(self.dev_dir, self.sys_dir)

            cons.print("Success.")

        except Exception as e:
            cons.print(e)

dotfiles = Dotfiles()
