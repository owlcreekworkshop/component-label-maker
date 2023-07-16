import pytest

from labelmaker.component.component_value import ComponentValue
from labelmaker.component.capacitor_value import CapacitorValue


def test_init():
    decorate = ComponentValue("1")
    subject = CapacitorValue(decorate)
    assert subject.decorated is decorate


def test_init_str():
    subject = CapacitorValue("1")
    assert type(subject.decorated) is ComponentValue


def test_get_value():
    subject = CapacitorValue("100")
    assert subject.get_value_formatted() == "100F"


def test_cast_str():
    subject = CapacitorValue(100)
    assert str(subject) == "100F"


test_code_data = [
    ("9p", None),
    ("10p", "100"),
    ("100p", "101"),
    ("99u", "996"),
    ("100u", None),
]


@pytest.mark.parametrize("value,expected", test_code_data)
def test_code_is_none(value: str, expected: str):
    subject = CapacitorValue(value)
    assert subject.get_code() == expected
