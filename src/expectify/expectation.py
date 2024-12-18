from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .matchers import Matcher


class Expectation:
    def __init__(self, subject) -> None:
        self._subject = subject

    def to(self, matcher: "Matcher") -> None:
        print(f"... check for matcher: {matcher}.")

        self._assert(matcher)

    def _assert(self, matcher) -> None:
        self._match(matcher)

    def _match(self, matcher) -> None:
        print(f"Attempting assert based on {matcher}")

        return getattr(matcher, "_match")(self._subject)
