from rich.progress import track
from rich.console import Console
console = Console()
sequence = range(100)
track(sequence=sequence, show_speed=True)
