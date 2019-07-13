from pathlib import Path


class Event:
    def __init__(self, path: Path):
        self.path = path

    def __str__(self):
        return str(self.path)


def get_events_in_dir(dir: Path):
    for event_file in dir.iterdir():
        if event_file.match("*.md") and event_file.is_file():
            yield Event(event_file)
        if event_file.is_dir():
            yield from get_events_in_dir(event_file)
