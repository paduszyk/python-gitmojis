# Contributing Guide

First of all, thank you for your interest in the project! 💚

You are welcome to contribute by:

* opening an issue to report bugs or request features;
* creating a pull request to fix a bug or implement a new feature;
* participating in discussions on the existing issues and PRs.

Whether you're opening an issue or creating a pull request, make sure to apply
our forms and templates as well as to follow the instructions and checklists
you'll find therein.

> If you are unfamiliar with contributing to open-source projects, consider
> taking a look at the official [GitHub docs][github-docs] or other related
> guides and assets, e.g., [First Contribution][first-contribution].

## Issues

There are several types of issues one can [open][open-issue] to contribute to
the project:

* 🐛 [Bug report][open-bug-report]
* ✨ [Feature request][open-feature-request]
* 🍻 [Discussions][open-discussion]

An issue of each type can be created using a specific form. Irrespective of the
issue type, contributors are requested to confirm that they are familiar with
this guide and the project's [Code of Conduct][code-of-conduct], as well as
that the issue they open is not a duplicate.

## Pull Requests

If you're looking to make small tweaks, especially in the docs or similar, feel
free to jump straight to creating a pull request. But if it's something more
substantial, like reporting a bug or suggesting a new feature, it's better to
start off by opening an issue. This gives everyone in the community a chance to
chime in and make sure we're all on the same page. Once there's a general
agreement, you can go ahead and submit your pull request.

When creating each pull request, it is crucial to adhere to the provided
instructions:

01. [Fork][fork] the repo and clone it to your machine.
02. Go to the project's root directory and sync development dependencies with
    [uv][uv]:

    ```console
    $ uv sync --locked
    ```

    > The command above creates a local virtual environment (`.venv`) and
    > installs all dependencies required for development. If a compatible
    > Python version is not available on your machine, `uv` will resolve and
    > install one automatically.

03. Install [Pre-commit][pre-commit] hooks:

    ```console
    $ uv run pre-commit install
    ```

04. Run linters and tests using [Nox][nox]:

    ```console
    $ uv run nox
    ```

    This will check your fork's setup, the code quality with linters, run the
    existing tests in different Python environments, and measure the coverage.

    If you want to be more specific, you can only run the linting or testing
    suites via the respective Nox sessions. All the available sessions can be
    listed using the command:

    ```console
    $ uv run nox -l
    ```

    For more details, see [`noxfile.py`][noxfile] and [Nox docs][nox-docs].
    Besides, note that all the linters and testing tools are installed in the
    local uv-managed virtual environment. Therefore, feel absolutely free to
    invoke them independently of Nox via `uv run`, e.g., `uv run ruff check .`.

05. Check out a new feature branch and introduce changes.

    > All the changes affecting the codebase must be accompanied by relevant
    > unit tests and documentation updates. We always attempt to maintain 100%
    > test coverage, and we require that from all pull requests as well. Those
    > with tests missing (if they are needed, of course) have exactly zero
    > chance of being merged!

06. Run Nox.

    If all the Nox sessions are successful and the changes are covered by tests,
    commit your changes and push them to remote.

    > Keep in mind that when you create a pull request, the CI will run all the
    > Nox sessions anyway. Nevertheless, it is still strongly recommended to
    > test everything locally before pushing to remote and opening a pull
    > request.

07. [Create a pull request][create-pull-request] from the feature branch of your
    fork to the `main` branch of the original repository.

    > Don't forget to mark the pull request with an appropriate Gitmoji! 😜

That's it! 🎉

As soon as your pull request passes all CI checks, it will be reviewed by the
project's maintainers as soon as possible. 🧐

[code-of-conduct]: https://github.com/paduszyk/python-gitmojis/blob/main/.github/CODE_OF_CONDUCT.md
[create-pull-request]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
[first-contribution]: https://github.com/firstcontributions/first-contributions
[fork]: https://docs.github.com/en/get-started/quickstart/fork-a-repo
[github-docs]: https://docs.github.com/en/get-started/quickstart/contributing-to-projects
[nox]: https://github.com/wntrblm/nox
[nox-docs]: https://nox.thea.codes/en/stable/usage.html#command-line-usage
[noxfile]: https://github.com/paduszyk/python-gitmojis/blob/main/noxfile.py
[open-bug-report]: https://github.com/paduszyk/python-gitmojis/issues/new?template=bug-report.yml
[open-discussion]: https://github.com/paduszyk/python-gitmojis/issues/new?template=discussion.yml
[open-feature-request]: https://github.com/paduszyk/python-gitmojis/issues/new?template=feature-request.yml
[open-issue]: https://github.com/paduszyk/python-gitmojis/issues/new/choose
[pre-commit]: https://pre-commit.com
[uv]: https://docs.astral.sh/uv/
