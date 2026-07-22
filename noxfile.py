import nox
import nox_uv

# Nox sessions and configuration
# https://nox.thea.codes/en/stable/config.html

nox.options.default_venv_backend = "uv"


@nox_uv.session(uv_only_groups=["black"])
def black(session: nox.Session) -> None:
    session.run("black", "--check", "--diff", ".")


@nox_uv.session(uv_groups=["mypy"])
def mypy(session: nox.Session) -> None:
    session.run("mypy", "--install-types", "--non-interactive", ".")


@nox_uv.session(uv_only_groups=["ruff"])
def ruff(session: nox.Session) -> None:
    session.run("ruff", "check", "--diff", ".")


@nox_uv.session(
    uv_groups=["test"],
    python=[
        "3.10",
        "3.11",
        "3.12",
        "3.13",
        "3.14",
    ],
)
def test(session: nox.Session) -> None:
    session.run("pytest")
