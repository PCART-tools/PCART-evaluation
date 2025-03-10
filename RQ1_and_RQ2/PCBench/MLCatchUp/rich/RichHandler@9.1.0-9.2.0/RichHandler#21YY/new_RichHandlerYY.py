import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(highlighter=ReprHighlighter(), enable_link_path=True, tracebacks_extra_lines=3, show_path=True, tracebacks_width=80, show_time=True, markup=False, show_level=True, rich_tracebacks=True, tracebacks_theme='monokai', tracebacks_show_locals=False)
