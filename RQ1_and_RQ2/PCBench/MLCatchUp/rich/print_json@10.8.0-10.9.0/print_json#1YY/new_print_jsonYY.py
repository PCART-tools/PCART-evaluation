from rich.console import Console
console = Console()
json_str = '{"name": "John", "age": 30, "city": "New York"}'
console.print_json(json_str, json=None, data=None, indent=2)
