import click
command = click.Command('my_command', None, callback=None, params=[click.Option(['--param'], default=42)], help=None, epilog=None, no_args_is_help=False)
