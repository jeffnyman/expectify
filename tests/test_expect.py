import pytest

from expectify import expect, equal


def test_expect_equal_pass() -> None:
    expect("jeff").to(equal("jeff"))


def test_expect_equal_fail() -> None:
    with pytest.raises(AssertionError):
        expect("jeff").to(equal("geoff"))


def test_expect_negated_equal_pass():
    expect("jeff").not_to(equal("geoff"))


def test_expect_negated_equal_variant_pass():
    expect("jeff").to_not(equal("geoff"))
