import http.server
import os
import webbrowser
from pathlib import Path

import click


def serve_output(output_dir: Path, open_in_browser=True):
    server = http.server.HTTPServer(("", 8000), http.server.SimpleHTTPRequestHandler)
    click.echo("Serving {} on port 8000".format(output_dir))
    os.chdir(str(output_dir))
    if open_in_browser:
        webbrowser.open("http://localhost:8000")
    server.serve_forever()
