from pathlib import Path

from .logger import logger

class FileSystem:
    def __init__(self):
        self.home = Path(__file__).resolve().home()
        self.project = Path(__file__).resolve().parent
        self.deps = self.project / "deps.yaml"
        self.config = self.home / ".config"
        self.cache = self.home / ".cache"
        self.share = self.home / ".local/share"
        self.bin = self.home / ".local/bin"
        self.state = self.home / ".local/state"
    
    def ping_folders(self):
        logger.ping(f"(Home Folder)     [cyan]{fs.home}[/cyan]")
        logger.ping(f"(Project Folder)  [cyan]{fs.project}[/cyan]")
        logger.ping(f"(Deps Folder)     [cyan]{fs.deps}[/cyan]")
        logger.ping(f"(Config Folder)   [cyan]{fs.config}[/cyan]")
        logger.ping(f"(Cache Folder)    [cyan]{fs.cache}[/cyan]")
        logger.ping(f"(Share Folder)    [cyan]{fs.share}[/cyan]")
        logger.ping(f"(Bin Folder)      [cyan]{fs.bin}[/cyan]")
        logger.ping(f"(State Folder)    [cyan]{fs.state}[/cyan]")


fs = FileSystem()
