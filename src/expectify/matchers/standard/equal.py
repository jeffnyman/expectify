from typing import Any, Never
from .. import Matcher


class equal(Matcher):
    def __init__(self, expected: int | str) -> None:
        self._expected: int | str = expected

    def _match(self, subject: int | str) -> tuple[Any, list[Never]]:
        return subject == self._expected, []

    def _match_negated(self, subject: int | str) -> tuple[Any, list[Never]]:
        return subject != self._expected, []
