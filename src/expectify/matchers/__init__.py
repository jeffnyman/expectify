class Matcher:
    def _failure_message(self, subject: str, reasons: list) -> str:
        return f"Expected: {subject}; {self}; {reasons}"

    def __repr__(self) -> str:
        return self._name

    @property
    def _name(self) -> str:
        return type(self).__name__
