class Expectation:
    def __init__(self, subject):
        self._subject = subject
        self._negated = False

    def to(self, matcher):
        __tracebackhide__ = True

        self._assert(matcher)

    @property
    def not_to(self):
        __tracebackhide__ = True

        self._negated = True
        return self.to

    @property
    def to_not(self):
        __tracebackhide__ = True

        return self.not_to

    def _assert(self, matcher):
        __tracebackhide__ = True

        passed, reasons = self._match(matcher)

        if not passed:
            raise AssertionError(self._failure_reason(matcher, reasons))

    def _match(self, matcher):
        if self._negated:
            return matcher.match_negated(self._subject)
        else:
            return matcher.match(self._subject)

    def _failure_reason(self, matcher, *args):
        if self._negated:
            return matcher.failure_message_negated(self._subject, *args)
        else:
            return matcher.failure_message(self._subject, *args)
