from rich.console import Console
console = Console()
json_str = '{"name": "John", "age": 30, "city": "New York"}'
console.print_json(json=json_str, highlight=True, json=None, data=None, indent=2)
