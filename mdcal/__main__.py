import time
from pathlib import Path
from shutil import copytree, rmtree

import click
from ics import Calendar

from mdcal import MODULE_DIR

from .event import get_events_in_dir
from .html_calendar import save_html_calendar
from .server import serve_output


@click.command()
@click.argument(
    "input_dir",
    type=click.Path(exists=True, file_okay=False, readable=True, resolve_path=True),
)
@click.argument(
    "output_dir", type=click.Path(file_okay=False, writable=True, resolve_path=True)
)
@click.option("--serve", is_flag=True)
def main(input_dir, output_dir, serve):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    start_time = time.time()

    output_dir.mkdir(parents=True, exist_ok=True)

    calendar = Calendar(creator="mdcal")
    events = list(get_events_in_dir(input_dir))
    with click.progressbar(events, label="Adding events to ical calendar") as bar:
        for event in bar:
            calendar.events.add(event.to_ics_event())
    click.echo("Saving ical calendar...")
    output_dir.joinpath("index.ics").write_text(str(calendar))
    click.echo("Saving html calendar...")
    save_html_calendar(output_dir, events)
    click.echo("Exporting static files...")

    rmtree(str(output_dir.joinpath("static")), ignore_errors=True)
    copytree(str(MODULE_DIR.joinpath("static")), str(output_dir.joinpath("static")))

    click.echo("Completed in {}s".format(round(time.time() - start_time, 3)))

    if serve:
        serve_output(output_dir)
