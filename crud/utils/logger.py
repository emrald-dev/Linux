from rich.console import Console

cons = Console()

class Logger():
    def __init__(self):
        pass

    def ping(self, msg):
        cons.print(f"[bold green]PING[/bold green]: {msg}")

logger = Logger()
