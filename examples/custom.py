from expectify.matchers import Matcher


class have_content(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, content):
        if self._expected in content:
            return True, ["content found"]

        return False, ["content not found"]
