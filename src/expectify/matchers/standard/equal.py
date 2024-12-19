from typing import Any, Never, Union
from .. import Matcher


class equal(Matcher):
    def __init__(self, expected: Union[int, str]) -> None:
        self._expected: Union[int, str] = expected

    def _match(self, subject: str) -> tuple[Any, list[Never]]:
        return subject == self._expected, []

    def _match_negated(self, subject: str) -> tuple[Any, list[Never]]:
        return subject != self._expected, []
