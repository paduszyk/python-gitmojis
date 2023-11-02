import click

from gitmojis.core import fetch_guide


@click.group(
    name="gitmojis",
)
@click.version_option(
    package_name="python-gitmojis",
    prog_name="gitmojis",
)
@click.pass_context
def gitmojis_cli(context: click.Context) -> None:
    """Command-line interface for managing the official Gitmoji guide."""
    # Initialize the context object
    context.ensure_object(dict)

    # Pass the current state of the Gitmoji guide to the group context
    context.obj["guide"] = fetch_guide()
