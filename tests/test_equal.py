import pytest

from expectify import expect
from expectify.matchers.built_in.equal import equal


def test_expect_equal_pass():
    expect("jeff").to(equal("jeff"))


def test_expect_negated_equal_pass():
    expect("jeff").not_to(equal("geoff"))


def test_expect_equal_fail():
    with pytest.raises(AssertionError):
        expect("jeff").to(equal("geoff"))
