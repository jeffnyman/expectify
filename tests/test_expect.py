from expectify import expect, equal


def test_expect() -> None:
    expect("jeff").to(equal("jeff"))
