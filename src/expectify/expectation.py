from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from .matchers import Matcher


class Expectation:
    def __init__(self, subject) -> None:
        self._subject = subject
        self._negated: bool = False

    def to(self, matcher: "Matcher") -> None:
        __tracebackhide__ = True

        self._assert(matcher)

    @property
    def not_to(self) -> Callable[["Matcher"], None]:
        __tracebackhide__ = True

        self._negated = True

        return self.to

    @property
    def to_not(self) -> Callable[["Matcher"], None]:
        __tracebackhide__ = True

        return self.not_to

    def _assert(self, matcher: "Matcher") -> None:
        __tracebackhide__ = True

        passed, reasons = self._match(matcher)

        if not passed:
            raise AssertionError(self._failure_reason(matcher, reasons))

    def _match(self, matcher: "Matcher") -> tuple:
        if self._negated:
            return matcher._match_negated(self._subject)
        else:
            return matcher._match(self._subject)

    def _failure_reason(self, matcher: "Matcher", *reasons: list) -> str:
        if self._negated:
            return matcher._failure_message_negated(self._subject, *reasons)
        else:
            return matcher._failure_message(self._subject, *reasons)
