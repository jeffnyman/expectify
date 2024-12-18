from .. import Matcher


class equal(Matcher):
    def __init__(self, expected):
        self._expected = expected
