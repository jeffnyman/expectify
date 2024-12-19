import pytest

from expectify import expect, equal


def test_expect_equal_pass() -> None:
    expect("jeff").to(equal("jeff"))
    expect(1).to(equal(1))


def test_expect_equal_fail() -> None:
    with pytest.raises(AssertionError):
        expect("jeff").to(equal("geoff"))
        expect(1).to(equal(2))
        expect(1).not_to(equal(1))


def test_expect_negated_equal_pass():
    expect("jeff").not_to(equal("geoff"))
    expect(1).not_to(equal(2))


def test_expect_negated_equal_variant_pass():
    expect("jeff").to_not(equal("geoff"))
