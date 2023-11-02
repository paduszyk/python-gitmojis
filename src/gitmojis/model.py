from collections import UserList
from dataclasses import dataclass
from typing import Iterable, Literal


@dataclass(frozen=True, kw_only=True)
class Gitmoji:
    emoji: str
    entity: str
    code: str
    description: str
    name: str
    semver: Literal["major", "minor", "patch"] | None


class Guide(UserList[Gitmoji]):
    def __init__(self, *, gitmojis: Iterable[Gitmoji] | None = None) -> None:
        super().__init__(gitmojis)

    @property
    def gitmojis(self) -> list[Gitmoji]:
        return self.data
