import click


@click.command()
@click.argument(
    "input_dir",
    type=click.Path(exists=True, file_okay=False, readable=True, resolve_path=True),
)
@click.argument(
    "output_dir", type=click.Path(file_okay=False, writable=True, resolve_path=True)
)
def main(input_dir, output_dir):
    print("Hello world", input_dir, output_dir)
