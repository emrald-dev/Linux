from pathlib import Path

from .logger import logger

class FileSystem:
    def __init__(self):
        self.home = Path(__file__).resolve().home()
        self.config = self.home / ".config"
        self.cache = self.home / ".cache"
        self.share = self.home / ".local/share"
        self.bin = self.home / ".local/bin"
        self.state = self.home / ".local/state"

        self.dev = self.home / "Workspace/Linux"
        self.deps = self.dev / ".linux/deps.yaml"

    def ping_folders(self):
        logger.ping(f"(Home Folder)     [cyan]{fs.home}[/cyan]")
        logger.ping(f"(Config Folder)   [cyan]{fs.config}[/cyan]")
        logger.ping(f"(Cache Folder)    [cyan]{fs.cache}[/cyan]")
        logger.ping(f"(Share Folder)    [cyan]{fs.share}[/cyan]")
        logger.ping(f"(Bin Folder)      [cyan]{fs.bin}[/cyan]")
        logger.ping(f"(State Folder)    [cyan]{fs.state}[/cyan]")

        logger.ping(f"(Project Folder)  [cyan]{fs.dev}[/cyan]")


fs = FileSystem()
