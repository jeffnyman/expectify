from typing import Union
from .expectation import Expectation


def expect(subject: Union[int, str]) -> Expectation:
    print(f"Expect called for {subject}.")

    return Expectation(subject)
