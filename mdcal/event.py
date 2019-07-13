from pathlib import Path
import hashlib

from dateutil.parser import parse
from markdown import Markdown
from ics import Event as ICSEvent
import datetime


class Event:
    def __init__(self, path: Path):
        self.path = path
        md = Markdown(extensions=["meta"])
        self.content = md.convert(path.read_text())
        self.metadata = md.Meta  # type: dict
        self.name = self.metadata.pop("name")[0]
        self.date = parse(self.metadata.pop("date")[0])

    @property
    def end_date(self):
        if "end_date" in self.metadata:
            return parse(self.metadata.pop("end_date")[0])
        return None

    def is_all_day(self):
        if self.end_date is None and self.date.time() == datetime.time(0, 0, 0):
            return True
        if self.end_date == self.date:
            return True
        return False

    @property
    def id(self):
        hasher = hashlib.sha1()
        hasher.update(str(self.path).encode())
        return hasher.hexdigest()

    def __str__(self):
        return "{}: {} @ {}".format(self.id, self.name, self.date)

    def to_ics_event(self):
        ics_event = ICSEvent(
            name=self.name,
            begin=self.date,
            end=self.end_date,
            uid=self.id,
            created=self.path.stat().st_ctime,
            description=self.content or None
        )
        if self.is_all_day():
            ics_event.make_all_day()
        return ics_event


def get_events_in_dir(dir: Path):
    for event_file in dir.iterdir():
        if event_file.match("*.md") and event_file.is_file():
            yield Event(event_file)
        if event_file.is_dir():
            yield from get_events_in_dir(event_file)
