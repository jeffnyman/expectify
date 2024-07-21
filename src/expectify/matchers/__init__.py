class Matcher:
    def _match(self, subject):
        raise NotImplementedError()

    def _failure_message(self, subject, reasons):
        message = "\nexpected: {subject!r} to {matcher!r}".format(
            subject=subject, matcher=self)

        if reasons:
            message += "\n     but: {0}".format("\n          ".join(reasons))

        return message

    def __repr__(self):
        if hasattr(self, "_expected"):
            return "{name} {expected!r}".format(name=self._name, expected=self._expected)

        return self._name

    @property
    def _name(self):
        return type(self).__name__.replace("_", " ").strip()
