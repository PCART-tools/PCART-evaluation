from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED
from rich import print
renderable = Text('Hello, World!', justify='center')
panel = Panel(renderable, padding=(0, 0), safe_box=None, expand=True, width=None, style='none', border_style='none')
