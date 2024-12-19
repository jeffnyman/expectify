import pytest

from expectify import expect, equal, be_true


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


def test_expect_be_true_pass() -> None:
    expect(True).to(be_true)
    expect(False).not_to(be_true)


def test_expect_be_true_fail() -> None:
    with pytest.raises(AssertionError):
        expect(True).not_to(be_true)
