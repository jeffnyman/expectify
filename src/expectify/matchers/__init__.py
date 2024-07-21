class Matcher:
    def _match(self, subject):
        raise NotImplementedError()

    def _failure_message(self, subject, reasons):
        message = "\nexpected: {subject!r} to {matcher!r}".format(
            subject=subject, matcher=self)

        if reasons:
            message += "\n     but: {0}".format("\n          ".join(reasons))

        return message
