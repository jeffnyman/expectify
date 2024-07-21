class Expectation:
    def __init__(self, subject):
        self._subject = subject

    def to(self, matcher):
        self._assert(matcher)

    def _assert(self, matcher):
        passed, reasons = self._match(matcher)

        if not passed:
            raise AssertionError(self._failure_reason(matcher, reasons))

    def _match(self, matcher):
        return getattr(matcher, "_match")(self._subject)

    def _failure_reason(self, matcher, *args):
        return getattr(matcher, "_failure_message")(self._subject, *args)
