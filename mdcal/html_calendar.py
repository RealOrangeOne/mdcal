import json
from pathlib import Path
from typing import Dict, List

from jinja2 import Template

from mdcal import MODULE_DIR
from mdcal.event import Event


def save_html_calendar(output_dir: Path, events: List[Event], calendar_config: Dict):
    events_as_dict = [event.as_dict() for event in events]
    template = Template(MODULE_DIR.joinpath("templates", "calendar.html").read_text())
    output_dir.joinpath("index.html").write_text(
        template.render(events=events_as_dict, calendar=calendar_config)
    )

    with output_dir.joinpath("events.json").open("w") as f:
        json.dump(events_as_dict, f)
