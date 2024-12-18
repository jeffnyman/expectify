class Matcher:
    def _failure_message(self, subject: str, reasons: list) -> str:
        return f"Expected: {subject}; {self}; {reasons}"
