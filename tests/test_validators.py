"""
test_validators.py — parametrized tests for password, age, and divide.
Demonstrates: parametrize, pytest.param, xfail, skip, pytest.raises, markers.
"""
import pytest
from src.validators import is_valid_password, is_valid_age, divide


# ── Password validation ────────────────────────────────────────────────────────

@pytest.mark.smoke
@pytest.mark.parametrize("password, expected", [
    pytest.param("12345678",               True,  id="valid_min_boundary"),
    pytest.param("12345678901234567890",   True,  id="valid_max_boundary"),
    pytest.param("validpass",             True,  id="valid_middle"),
    pytest.param("1234567",               False, id="invalid_too_short"),
    pytest.param("123456789012345678901", False, id="invalid_too_long"),
    pytest.param("",                      False, id="invalid_empty",
                 marks=pytest.mark.xfail(reason="empty string edge case not yet handled")),
    pytest.param("hello world",           False, id="invalid_spaces",
                 marks=pytest.mark.skip(reason="whitespace rule not yet defined")),
])
def test_is_valid_password(password, expected):
    assert is_valid_password(password) == expected


# ── Age validation ─────────────────────────────────────────────────────────────

@pytest.mark.smoke
@pytest.mark.parametrize("age, expected", [
    pytest.param(18,  True,  id="valid_min_boundary"),
    pytest.param(99,  True,  id="valid_max_boundary"),
    pytest.param(25,  True,  id="valid_middle"),
    pytest.param(17,  False, id="invalid_underage"),
    pytest.param(100, False, id="invalid_over_max"),
    pytest.param(0,   False, id="invalid_zero"),
])
def test_is_valid_age(age, expected):
    assert is_valid_age(age) == expected


# ── Divide ─────────────────────────────────────────────────────────────────────

@pytest.mark.regression
@pytest.mark.parametrize("a, b, expected", [
    pytest.param(10, 2,   5.0,  id="normal_division"),
    pytest.param(9,  3,   3.0,  id="clean_division"),
    pytest.param(-6, 2,  -3.0,  id="negative_numerator"),
    pytest.param(7,  2,   3.5,  id="float_result"),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


@pytest.mark.regression
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
