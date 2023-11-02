import subprocess
import sys

import click

from gitmojis.cli import commands as commands_module
from gitmojis.cli import get_commands, gitmojis_cli
from gitmojis.model import Guide


def test_gitmojis_cli_runs_from_package_main_module():
    result = subprocess.run([sys.executable, "-m", "gitmojis"])

    assert result.returncode == 0


def test_get_commands_registers_command_from_commands_module(mocker):
    @click.command()
    def command():
        pass

    mocker.patch.dict(commands_module.__dict__, {"command": command})

    commands = get_commands()

    assert command in commands


def test_gitmojis_cli_passes_guide_to_context(mocker, cli_runner):
    mocker.patch("gitmojis.core.fetch_guide", return_value=Guide(gitmojis=[]))

    @click.command()
    @click.pass_context
    def command(context):
        assert "guide" in context.obj

    gitmojis_cli.add_command(command)

    result = cli_runner.invoke(gitmojis_cli, "command")

    assert result.exit_code == 0
