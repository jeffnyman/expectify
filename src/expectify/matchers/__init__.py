class Matcher:
    def match(self, subject):
        raise NotImplementedError

    def failure_message(self, subject, reasons):
        message = f"\nexpected: {subject!r} to {self!r}"

        if reasons:
            message += f"\n     but: {'\n          '.join(reasons)}"

        return message

    def __repr__(self):
        if hasattr(self, "_expected"):
            return f"{self._name} {self._expected!r}"

        return self._name

    @property
    def _name(self):
        return type(self).__name__.replace("_", " ").strip()
