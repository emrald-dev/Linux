from pathlib import Path
from rich.console import Console


root = Path(__file__).resolve().parent
deps = root / "deps.yaml"
cons = Console()

