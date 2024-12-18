from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .matchers import Matcher


class Expectation:
    def __init__(self, subject) -> None:
        self._subject = subject

    def to(self, matcher: "Matcher") -> None:
        self._assert(matcher)

    def _assert(self, matcher: "Matcher") -> None:
        passed, reasons = self._match(matcher)

        if not passed:
            raise AssertionError(self._failure_reason(matcher, reasons))

    def _match(self, matcher: "Matcher") -> tuple:
        return getattr(matcher, "_match")(self._subject)

    def _failure_reason(self, matcher: "Matcher", *reasons: list) -> tuple:
        return getattr(matcher, "_failure_message")(self._subject, *reasons)
