from pathlib import Path
from rich.console import Console

cons = Console()

class Logger():
    def __init__(self):
        pass

    def ping(self, msg):
        cons.print(f"[bold green]PING[/bold green]: {msg}")

logger = Logger()

class FileSystem:
    def __init__(self):
        self.home = Path(__file__).resolve().home()
        self.project = Path(__file__).resolve().parent
        self.deps = self.project / "deps.yaml"

fs = FileSystem()

def update_dotfiles():
    cons.print("Attempting dotfiles update, please wait.")

    try:
        pass
    except:
        pass
