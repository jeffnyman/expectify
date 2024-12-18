class Expectation:
    def __init__(self, subject) -> None:
        self._subject = subject

    @staticmethod
    def to(matcher: str) -> None:
        print(f"... check for matcher: {matcher}.")
