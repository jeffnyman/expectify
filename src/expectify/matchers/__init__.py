class Matcher:
    def _failure_message(self, subject: str, reasons: list) -> str:
        message = f"\nexpected: {subject} to {self}"

        if reasons:
            newline = "\n          "
            message += f"\n     but: {newline.join(reasons)}"

        return message

    def _failure_message_negated(self, subject: str, reasons: list) -> str:
        message = f"\nexpected: {subject} not to {self}"

        if reasons:
            newline = "\n          "
            message += f"\n     but: {newline.join(reasons)}"

        return message

    def __repr__(self) -> str:
        if hasattr(self, "_expected"):
            return f"{self._name} {self._expected}"

        return self._name

    @property
    def _name(self) -> str:
        return type(self).__name__
