from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .matchers import Matcher


class Expectation:
    def __init__(self, subject) -> None:
        self._subject = subject

    @staticmethod
    def to(matcher: "Matcher") -> None:
        print(f"... check for matcher: {matcher}.")
