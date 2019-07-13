from pathlib import Path

import click

from .event import get_events_in_dir


@click.command()
@click.argument(
    "input_dir",
    type=click.Path(exists=True, file_okay=False, readable=True, resolve_path=True),
)
@click.argument(
    "output_dir", type=click.Path(file_okay=False, writable=True, resolve_path=True)
)
def main(input_dir, output_dir):
    for event in get_events_in_dir(Path(input_dir)):
        print(event)
