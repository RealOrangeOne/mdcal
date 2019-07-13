from pathlib import Path
import hashlib

from dateutil.parser import parse
from markdown import Markdown


class Event:
    def __init__(self, path: Path):
        self.path = path
        md = Markdown(extensions=["meta"])
        self.content = md.convert(path.read_text())
        self.metadata = md.Meta  # type: dict
        self.name = self.metadata.pop("name")[0]
        self.date = parse(self.metadata.pop("date")[0])

    @property
    def id(self):
        hasher = hashlib.sha1()
        hasher.update(str(self.path).encode())
        return hasher.hexdigest()

    def __str__(self):
        return "{}: {} @ {}".format(self.id, self.name, self.date)


def get_events_in_dir(dir: Path):
    for event_file in dir.iterdir():
        if event_file.match("*.md") and event_file.is_file():
            yield Event(event_file)
        if event_file.is_dir():
            yield from get_events_in_dir(event_file)
