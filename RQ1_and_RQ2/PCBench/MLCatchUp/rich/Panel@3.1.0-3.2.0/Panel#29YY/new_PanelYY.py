from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED
from rich import print
renderable = Text('Hello, World!', justify='center')
panel = Panel(renderable, ROUNDED, expand=True, safe_box=None, width=None, style='none', border_style='none')
