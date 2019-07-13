from pathlib import Path

import click

from .event import get_events_in_dir
from ics import Calendar


@click.command()
@click.argument(
    "input_dir",
    type=click.Path(exists=True, file_okay=False, readable=True, resolve_path=True),
)
@click.argument(
    "output_dir", type=click.Path(file_okay=False, writable=True, resolve_path=True)
)
def main(input_dir, output_dir):
    calendar = Calendar(creator="mdcal")
    with click.progressbar(get_events_in_dir(Path(input_dir)), label="Generating events") as bar:
        for event in bar:
            calendar.events.add(event.to_ics_event())
    print(str(calendar))
