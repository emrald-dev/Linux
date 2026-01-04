from pathlib import Path

from .logger import logger

class FileSystem:
    def __init__(self):
        self.home = Path(__file__).resolve().home()
        self.project = Path(__file__).resolve().parent
        self.deps = self.project / "deps.yaml"
        self.config = self.home / ".config"
    
    def ping_folders(self):
        logger.ping(f"(Home Folder)     [cyan]{fs.home}[/cyan]")
        logger.ping(f"(Project Folder)  [cyan]{fs.project}[/cyan]")
        logger.ping(f"(Deps Folder)     [cyan]{fs.deps}[/cyan]")
        logger.ping(f"(Config Folder)   [cyan]{fs.config}[/cyan]")

fs = FileSystem()
