import sys
from pathlib import Path

import tomllib


def get_package_version() -> str:
    """Return the package version from the `pyproject.toml` metadata."""
    with (Path.cwd() / "pyproject.toml").open("rb") as pyproject_toml:
        metadata = tomllib.load(pyproject_toml)
    return metadata["project"]["version"]


if __name__ == "__main__":
    sys.stdout.write(get_package_version())
