import nox

# Nox sessions and configuration
# https://nox.thea.codes/en/stable/config.html


@nox.session()
def black(session: nox.Session) -> None:
    session.install("black")
    session.run("black", "--check", "--diff", ".")


@nox.session()
def mypy(session: nox.Session) -> None:
    session.install("-e", ".")
    session.install("mypy")
    session.run("mypy", "--install-types", "--non-interactive", ".")


@nox.session()
def ruff(session: nox.Session) -> None:
    session.install("ruff")
    session.run("ruff", "check", "--diff", ".")


@nox.session(
    python=[
        "3.10",
        "3.11",
        "3.12",
    ]
)
def test(session: nox.Session) -> None:
    session.install("-e", ".[test]")
    session.run("pytest")
