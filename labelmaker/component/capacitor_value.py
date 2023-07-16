import math

from labelmaker.component.component_value import ComponentValue


class CapacitorValue():
    def __init__(self, value: ComponentValue):
        if type(value) == ComponentValue:
            self.decorated = value
        else:
            self.decorated = ComponentValue(value)

    def __str__(self) -> str:
        return self.decorated.__str__() + "F"

    def get_value(self, suffix: str = None) -> float:
        return self.decorated.get_value(suffix)

    def get_exp(self) -> float:
        return self.decorated.get_exp()

    def get_value_formatted(self, suffix: str = None, places: int = 2) -> str:
        return self.decorated.get_value_formatted(suffix, places) + "F"

    def set_value(self, value: any):
        self.decorated.set_value(value)

    def get_value_alternates_formatted(self):
        exp = self.get_exp()

        return [
            self.get_value_formatted(self.decorated._get_suffix_for_exp(exp + 3), 6),
            self.get_value_formatted(self.decorated._get_suffix_for_exp(exp - 3), 6),
        ]

    def get_code(self):
        pico = self.get_value("p")
        if pico < 10:
            return None

        if pico >= 100000000:
            return None

        exp = math.floor(math.log10(pico))-1
        return (f"{int(pico * math.pow(10, -exp))}{exp}")
