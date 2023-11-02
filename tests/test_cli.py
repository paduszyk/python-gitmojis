import click

from gitmojis.cli import gitmojis_cli
from gitmojis.model import Guide


def test_gitmojis_cli_passes_guide_to_context(mocker, cli_runner):
    mocker.patch("gitmojis.core.fetch_guide", return_value=Guide(gitmojis=[]))

    @click.command()
    @click.pass_context
    def command(context):
        assert "guide" in context.obj

    gitmojis_cli.add_command(command)

    result = cli_runner.invoke(gitmojis_cli, "command")

    assert result.exit_code == 0
