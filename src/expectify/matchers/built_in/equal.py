from .. import Matcher


class equal(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def match(self, subject):
        return subject == self._expected, []
