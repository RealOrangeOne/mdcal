import http.server
import os
from pathlib import Path

import click


def serve_output(output_dir: Path):
    server = http.server.HTTPServer(("", 8000), http.server.SimpleHTTPRequestHandler)
    click.echo("Serving {} on port 8000".format(output_dir))
    os.chdir(str(output_dir))
    server.serve_forever()
