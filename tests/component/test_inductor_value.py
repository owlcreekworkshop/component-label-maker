import pytest

from labelmaker.component.component_value import ComponentValue
from labelmaker.component.inductor_value import InductorValue


def test_init():
    subject = InductorValue("1")
    assert type(subject.decorated) is ComponentValue


def test_init_decorated():
    decorate = ComponentValue("1")
    subject = InductorValue(decorate)
    assert subject.decorated is decorate


init_data = [
    (1, 1),
    ("1", 1),
    (1.1, 1.1),
    (ComponentValue(1), 1)
]


@pytest.mark.parametrize("value,expected", init_data)
def test_init_value(value, expected):
    subject = InductorValue(value)
    assert subject.get_value() == expected


def test_get_value():
    subject = InductorValue("100")
    assert subject.get_value_formatted() == "100H"


def test_cast_str():
    subject = InductorValue(100)
    assert str(subject) == "100H"


stripe_data = [
    ("0.1u", [1, 0, 11]),
    ("1.1u", [1, 1, 10]),
    ("10u", [1, 0, 0]),
    ("20u", [2, 0, 0]),
    ("30u", [3, 0, 0]),
    ("40u", [4, 0, 0]),
    ("50u", [5, 0, 0]),
    ("60u", [6, 0, 0]),
    ("70u", [7, 0, 0]),
    ("80u", [8, 0, 0]),
    ("90u", [9, 0, 0]),
    ("11u", [1, 1, 0]),
    ("22u", [2, 2, 0]),
    ("33u", [3, 3, 0]),
    ("44u", [4, 4, 0]),
    ("55u", [5, 5, 0]),
    ("66u", [6, 6, 0]),
    ("77u", [7, 7, 0]),
    ("88u", [8, 8, 0]),
    ("99u", [9, 9, 0]),
    (0.0001, [1, 0, 1]),
    (0.001, [1, 0, 2]),
    (0.01, [1, 0, 3]),
    (0.1, [1, 0, 4]),
    (1, [1, 0, 5]),
    (10, [1, 0, 6]),
    (100, [1, 0, 7]),
    (1000, [1, 0, 8]),
    (10000, [1, 0, 9]),
]


@pytest.mark.parametrize("value,expected", stripe_data)
def test_get_color_bands(value, expected):
    subject = InductorValue(value)
    assert subject.get_color_bands() == expected
