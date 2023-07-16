import math

import pytest

from labelmaker.component.component_value import ComponentValue

get_value_data = [
    (1, 1),
    (1.005, 1.005),
    (0.1, 0.1),
    ("1", 1),
    ("1.005", 1.005),
    ("0.1", 0.1),
    (".1", 0.1),
    ("1E", 1E+18),
    ("1P", 1E+15),
    ("1T", 1E+12),
    ("1G", 1E+9),
    ("1M", 1E+6),
    ("1k", 1E+3),
    ("1m", 1E-3),
    ("1u", 1E-6),
    ("1\u03BC", 1E-6),
    ("1n", 1E-9),
    ("1p", 1E-12),
    ("1f", 1E-15),
    ("1a", 1E-18),
]


@pytest.mark.parametrize("value,expected", get_value_data)
def test_get_value(value, expected):
    subject = ComponentValue(value)
    assert subject.get_value() == expected


get_value_formatted_data = [
    (1E+18, "1E"),
    (1E+15, "1P"),
    (1E+12, "1T"),
    (1E+9, "1G"),
    (1E+6, "1M"),
    (1E+3, "1k"),
    (1E-3, "1m"),
    (1E-6, "1\u03BC"),
    (1E-9, "1n"),
    (1E-12, "1p"),
    (1E-15, "1f"),
    (1E-18, "1a"),
]


@pytest.mark.parametrize("value,expected", get_value_formatted_data)
def test_get_value_formatted(value, expected):
    subject = ComponentValue(value)
    assert subject.get_value_formatted() == expected


@pytest.mark.parametrize("value,expected", get_value_formatted_data)
def test_cast_str(value, expected):
    subject = ComponentValue(value)
    assert str(subject) == expected


get_value_formatted_places_data = [
    ("1.124923", 0, "1"),
    ("1.125999", 2, "1.13"),
    ("1.124999", 4, "1.125"),
]


@pytest.mark.parametrize("value,places,expected", get_value_formatted_places_data)
def test_get_value_places(value, places, expected):
    subject = ComponentValue(value)
    assert subject.get_value_formatted(places=places) == expected


get_value_formatted_prefix_data = [
    (1, "E", 1E-18),
    (1, "P", 1E-15),
    (1, "T", 1E-12),
    (1, "G", 1E-9),
    (1, "M", 1E-6),
    (1, "k", 1E-3),
    (1, "m", 1E+3),
    (1, "u", 1E+6),
    (1, "\u03BC", 1E+6),
    (1, "n", 1E+9),
    (1, "p", 1E+12),
    (1, "f", 1E+15),
    (1, "a", 1E+18),
]


@pytest.mark.parametrize("value,prefix,expected", get_value_formatted_prefix_data)
def test_cast_str_prefixed(value, prefix, expected):
    subject = ComponentValue(value)
    assert math.isclose(subject.get_value(prefix), expected)


get_exp_data = [
    (1E+18, 18),
    (1E+15, 15),
    (1E+12, 12),
    (1E+9, 9),
    (1E+6, 6),
    (1E+3, 3),
    (1E-3, -3),
    (1E-6, -6),
    (1E-9, -9),
    (1E-12, -12),
    (1E-15, -15),
    (1E-18, -18),
]


@pytest.mark.parametrize("value,expected", get_exp_data)
def test_get_exp(value, expected):
    subject = ComponentValue(value)
    assert subject.get_exp() == expected
