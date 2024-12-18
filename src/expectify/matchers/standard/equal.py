from .. import Matcher


class equal(Matcher):
    def __init__(self, expected) -> None:
        self._expected = expected
