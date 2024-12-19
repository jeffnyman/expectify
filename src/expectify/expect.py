from .expectation import Expectation


def expect(subject: int | str) -> Expectation:
    print(f"Expect called for {subject}.")

    return Expectation(subject)
