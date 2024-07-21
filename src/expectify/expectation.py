class Expectation:
    def __init__(self, subject):
        self._subject = subject

    def to(self, matcher):
        __tracebackhide__ = True

        self._assert(matcher)

    def _assert(self, matcher):
        __tracebackhide__ = True

        passed, reasons = self._match(matcher)

        if not passed:
            raise AssertionError(self._failure_reason(matcher, reasons))

    def _match(self, matcher):
        return matcher.match(self._subject)

    def _failure_reason(self, matcher, *args):
        return matcher.failure_message(self._subject, *args)
