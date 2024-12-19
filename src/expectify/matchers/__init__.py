class Matcher:
    def _failure_message(self, subject: str, reasons: list) -> str:
        message = "\nexpected: {subject} to {matcher}".format(
            subject=subject, matcher=self
        )

        if reasons:
            message += "\n     but: {0}".format("\n          ".join(reasons))

        return message

    def __repr__(self) -> str:
        if hasattr(self, "_expected"):
            return "{name} {expected}".format(name=self._name, expected=self._expected)

        return self._name

    @property
    def _name(self) -> str:
        return type(self).__name__
