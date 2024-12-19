from typing import Any, Never
from .. import Matcher


class equal(Matcher):
    def __init__(self, expected: str) -> None:
        self._expected: str = expected

    def _match(self, subject: str) -> tuple[Any, list[Never]]:
        return subject == self._expected, []

    def _match_negated(self, subject: str):
        return subject != self._expected, []
