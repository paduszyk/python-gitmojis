# python-gitmojis

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=flat-square&logo=pre-commit)][pre-commit.ci]
[![github-build-workflow](https://img.shields.io/github/actions/workflow/status/paduszyk/python-gitmojis/build-package.yml?style=flat-square&logo=github)][github-build-workflow]
[![codecov](https://img.shields.io/codecov/c/github/paduszyk/python-gitmojis?style=flat-square&logo=codecov)][codecov]

[![nox](https://img.shields.io/badge/%F0%9F%A6%8A-Nox-D85E00.svg?style=flat-square)][nox]
[![ruff](https://img.shields.io/endpoint?style=flat-square&url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)][ruff]
[![mypy](https://img.shields.io/badge/type--checked-mypy-blue?style=flat-square)][mypy]
[![black](https://img.shields.io/badge/code%20style-black-black?style=flat-square)][black]

[![pypi-status](https://img.shields.io/pypi/status/python-gitmojis?style=flat-square&logo=pypi&logoColor=white)][pypi]
[![pypi-version](https://img.shields.io/pypi/v/python-gitmojis?style=flat-square&logo=pypi&logoColor=white)][pypi]
[![pypi-python-version](https://img.shields.io/pypi/pyversions/python-gitmojis?style=flat-square&logo=python&logoColor=white)][pypi]
[![pypi-license](https://img.shields.io/pypi/l/python-gitmojis?style=flat-square&label=license)][pypi]

## Summary

This package provides a few simple utilities to apply the official
[Gitmoji Guide][gitmoji-website] in Python libraries. It may potentially serve
as a helper in projects related to version control systems, versioning, and
automatic changelog generation. Applications in automation tools for validating
commit and pull request messages seem feasible as well.

## Features

- Handle individual Gitmojis and their lists using Python classes. 👔
- Fetch Gitmoji data directly from the official [Gitmoji API][gitmoji-api]. 😜
- Graceful degradation: If the API is unavailable, fall back to backup data. 🦺

## Installation

It is recommended to install the package directly from PyPI using `pip`:

```console
$ pip install python-gitmojis
```

or any other dependency manager of your preference. After installation, the
package functionalities can be accessed by importing them from the `gitmojis`
module:

```python
import gitmojis
```

## Usage

### Data model

The data model incorporates two classes representing individual Gitmojis and
their collections ("guides"), namely, `Gitmoji` and `Guide`, respectively.

The classes are defined in `gitmojis.model`, but can also be accessed directly
from `gitmojis` as well:

```python
from gitmojis import Gitmoji, Guide
```

#### `gitmojis.model.Gitmoji`

The `Gitmoji` class is a Python `@dataclass` ([PEP 557][PEP-557]) that uses a
set of fields consistent with the [JSON schema][gitmoji-schema] proposed in the
original Gitmoji project, namely:

- `emoji: str` &ndash; the emoji character representing the Gitmoji;
- `entity: str` &ndash; the HTML entity of the Gitmoji;
- `code: str` &ndash; the emoji's code to be used in rendering Gitmojis in the
  Markdown documents;
- `description: str` &ndash; a short note on the type of changes represented by
  the commits or pull requests marked by the Gitmoji;
- `name: str` &ndash; a text identifier of the Gitmoji;
- `semver: str | None` &ndash; the [Semantic Versioning](https://semver.org)
  level affected by the changes marked with the Gitmoji; the allowed string
  values are `"major"`, `"minor"`, and `"patch"`.

The class can be used to create immutable objects representing individual
Gitmojis, for example:

```python
from gitmojis import Gitmoji

gitmoji = Gitmoji(
    emoji="🤖",
    entity="&#x1f916",
    code=":robot:",
    description="Add or update Dependabot configuration.",
    name="robot",
    semver=None,
)

assert gitmoji.emoji == "🤖"
```

> Note that when creating a new `Gitmoji` instance, all the `@dataclass` fields
> are required. Furthermore, they all must be passed as keyword arguments.

#### `gitmojis.model.Guide`

The `Guide` class aims to provide a custom list-like structure to manage a
collection of Gitmojis. Its instances are created simply by passing an iterable
of `Gitmoji` objects (as the `gitmojis` keyword argument) to the class
constructor:

```python
from gitmojis import Gitmoji, Guide

gitmojis_json = [
    {
        "emoji" : "🤖",
        "entity" : "&#x1f916",
        "code" : ":robot:",
        "description" : "Add or update Dependabot configuration.",
        "name" : "robot",
        "semver" : None,
    },
    # ...
]

guide = Guide(
    gitmojis=[Gitmoji(**gitmoji_json) for gitmoji_json in gitmojis_json]
)

assert guide[0].emoji == "🤖"
```

The class is based on `collections.UserList`. Currently, it doesn't override
any base class methods nor does it implement any custom functionality.

### Fetching Gitmojis from the API

The main package functionality is implemented as a plain Python function, named
`fetch_guide`. It can be imported either from `gitmojis` or directly from its
source, i.e. the `gitmojis.core` module.

Usage of the function is extremely easy. In the simplest case, it can be called
without any arguments:

```python
from gitmojis import fetch_guide

guide = fetch_guide()
```

The function uses the `requests` library to return a `Guide` instance containing
the current state of the official [Gitmoji API][gitmoji-api]. If the API is
inaccessible, the guide can be populated using the data retrieved from the local
backup file. Such behavior can be triggered by passing `True` as the value of
the `use_backup` keyword argument (it defaults to `False`):

```python
from gitmojis import fetch_guide

guide = fetch_guide(use_backup=True)  # will work even if you're offline
```

### Command-line interface (CLI)

The package comes with a simple CLI which can be run using the `gitmojis`
command:

```console
$ gitmojis
Usage: gitmojis [OPTIONS] COMMAND [ARGS]...

  Command-line interface for managing the official Gitmoji guide.

Options:
  --use-backup  Use the backup to fetch data if the API request fails.
  --version     Show the version and exit.
  --help        Show this message and exit.

Commands:
  sync  Synchronize the backup file with the current state of the API.
```

As seen, currently the CLI provides only the `sync` command which can be used
to update the Gitmoji data backup file to the current state of the official API
endpoint.

> Checking for the updates of the API state is compared to the backup file by
> executing the `sync` command at GitHub Actions runner every week. The
> respective workflow automatically applies the updates and opens a pull
> request introducing them to the codebase. We plan to do the version bump (on
> a patch level) upon merging each of such pull requests. Therefore, to stay
> tuned with the Gitmoji API backed up by this library, you should update
> the package systematically. This particularly concerns the developers, who
> work with local repositories most of the time.

## Contributing

This project is open-source and embraces contributions of all types. For
comprehensive instructions on how to contribute to the project, please refer to
our [Contributing Guide][contributing-guide].

We require all contributors to adhere to our [Code of Conduct][code-of-conduct].
While it may seem intricate at first glance, the essence is simple: treat
everyone with kindness! 🙂

## Credits

The idea of Gitmoji was originally proposed, developed, and maintained by
Carlos Cuesta ([@carloscuesta][github-carlosquesta]). For more information, see
the official [repository][gitmoji-repository] and [website][gitmoji-website] of
the project.

## Authors

Created by Kamil Paduszyński ([@paduszyk][github-paduszyk]).

## License

Released under the [MIT License][license].

[black]: https://github.com/psf/black
[code-of-conduct]: https://github.com/paduszyk/python-gitmojis/blob/main/.github/CODE_OF_CONDUCT.md
[codecov]: https://app.codecov.io/gh/paduszyk/python-gitmojis
[contributing-guide]: https://github.com/paduszyk/python-gitmojis/blob/main/.github/CONTRIBUTING.md
[github-build-workflow]: https://github.com/paduszyk/python-gitmojis/actions/workflows/build-package.yml
[github-carlosquesta]: https://github.com/carloscuesta
[github-paduszyk]: https://github.com/paduszyk
[gitmoji-api]: https://github.com/carloscuesta/gitmoji/tree/master/packages/gitmojis#api
[gitmoji-repository]: https://github.com/carloscuesta/gitmoji
[gitmoji-schema]: https://github.com/carloscuesta/gitmoji/blob/master/packages/gitmojis/src/schema.json
[gitmoji-website]: https://gitmoji.dev
[license]: https://github.com/paduszyk/python-gitmojis/blob/main/LICENSE
[mypy]: https://github.com/python/mypy
[nox]: https://github.com/wntrblm/nox
[pep-557]: https://peps.python.org/pep-0557/
[pre-commit.ci]: https://results.pre-commit.ci/latest/github/paduszyk/python-gitmojis/main
[pypi]: https://pypi.org/project/python-gitmojis/
[ruff]: https://github.com/astral-sh/ruff
