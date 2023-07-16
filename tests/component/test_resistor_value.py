import pytest

from labelmaker.component.component_value import ComponentValue
from labelmaker.component.resistor_value import ResistorValue


def test_init():
    subject = ResistorValue("1")
    assert type(subject.decorated) is ComponentValue


def test_init_decorated():
    decorate = ComponentValue("1")
    subject = ResistorValue(decorate)
    assert subject.decorated is decorate


init_data = [
    (1, 1),
    ("1", 1),
    (1.1, 1.1),
    (ComponentValue(1), 1)
]


@pytest.mark.parametrize("value,expected", init_data)
def test_init_value(value, expected):
    subject = ResistorValue(value)
    assert subject.get_value() == expected


def test_get_value():
    subject = ResistorValue("100")
    assert subject.get_value_formatted() == "100\u2126"


def test_cast_str():
    subject = ResistorValue(100)
    assert str(subject) == "100\u2126"


stripe3_data = [
    (0.1, [1, 0, 11]),
    (1.1, [1, 1, 10]),
    (1, [1, 0, 10]),
    (10, [1, 0, 0]),
    (20, [2, 0, 0]),
    (30, [3, 0, 0]),
    (40, [4, 0, 0]),
    (50, [5, 0, 0]),
    (60, [6, 0, 0]),
    (70, [7, 0, 0]),
    (80, [8, 0, 0]),
    (90, [9, 0, 0]),
    (11, [1, 1, 0]),
    (22, [2, 2, 0]),
    (33, [3, 3, 0]),
    (44, [4, 4, 0]),
    (55, [5, 5, 0]),
    (66, [6, 6, 0]),
    (77, [7, 7, 0]),
    (88, [8, 8, 0]),
    (99, [9, 9, 0]),
    (100, [1, 0, 1]),
    (1000, [1, 0, 2]),
    (10000, [1, 0, 3]),
    (100000, [1, 0, 4]),
    (1000000, [1, 0, 5]),
    (10000000, [1, 0, 6]),
    (100000000, [1, 0, 7]),
    (1000000000, [1, 0, 8]),
    (10000000000, [1, 0, 9]),
]


@pytest.mark.parametrize("value,expected", stripe3_data)
def test_get_color_bands_3(value, expected):
    subject = ResistorValue(value)
    assert subject.get_color_bands(3) == expected


stripe4_data = [
    (0.1, [1, 0, 0, 11]),
    (1.1, [1, 1, 0, 11]),
    (1, [1, 0, 0, 11]),
    (10, [1, 0, 0, 10]),
    (100, [1, 0, 0, 0]),
    (200, [2, 0, 0, 0]),
    (300, [3, 0, 0, 0]),
    (400, [4, 0, 0, 0]),
    (500, [5, 0, 0, 0]),
    (600, [6, 0, 0, 0]),
    (700, [7, 0, 0, 0]),
    (800, [8, 0, 0, 0]),
    (900, [9, 0, 0, 0]),
    (110, [1, 1, 0, 0]),
    (220, [2, 2, 0, 0]),
    (330, [3, 3, 0, 0]),
    (440, [4, 4, 0, 0]),
    (550, [5, 5, 0, 0]),
    (660, [6, 6, 0, 0]),
    (770, [7, 7, 0, 0]),
    (880, [8, 8, 0, 0]),
    (990, [9, 9, 0, 0]),
    (111, [1, 1, 1, 0]),
    (222, [2, 2, 2, 0]),
    (333, [3, 3, 3, 0]),
    (444, [4, 4, 4, 0]),
    (555, [5, 5, 5, 0]),
    (666, [6, 6, 6, 0]),
    (777, [7, 7, 7, 0]),
    (888, [8, 8, 8, 0]),
    (999, [9, 9, 9, 0]),
    (100, [1, 0, 0, 0]),
    (1000, [1, 0, 0, 1]),
    (10000, [1, 0, 0, 2]),
    (100000, [1, 0, 0, 3]),
    (1000000, [1, 0, 0, 4]),
    (10000000, [1, 0, 0, 5]),
    (100000000, [1, 0, 0, 6]),
    (1000000000, [1, 0, 0, 7]),
    (10000000000, [1, 0, 0, 8]),
    (100000000000, [1, 0, 0, 9]),
]


@pytest.mark.parametrize("value,expected", stripe4_data)
def test_get_color_bands_4(value, expected):
    subject = ResistorValue(value)
    assert subject.get_color_bands(4) == expected
