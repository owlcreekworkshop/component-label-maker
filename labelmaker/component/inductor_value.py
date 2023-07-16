import math

from labelmaker.component.component_value import ComponentValue


class InductorValue():
    def __init__(self, value: ComponentValue):
        if type(value) == ComponentValue:
            self.decorated = value
        else:
            self.decorated = ComponentValue(value)

    def __str__(self) -> str:
        return self.decorated.__str__() + "H"

    def get_value(self, suffix: str = None) -> float:
        return self.decorated.get_value(suffix)

    def get_value_formatted(self, suffix: str = None, places: int = 2) -> str:
        return self.decorated.get_value_formatted(suffix, places) + "H"

    def get_exp(self) -> float:
        return self.decorated.get_exp()

    def set_value(self, value: any):
        self.decorated.set_value(value)

    def get_value_alternates_formatted(self):
        exp = self.get_exp()

        return [
            self.get_value_formatted(self.decorated._get_suffix_for_exp(exp + 3), 6),
            self.get_value_formatted(self.decorated._get_suffix_for_exp(exp - 3), 6),
        ]

    def get_color_bands(self):
        val = round(self.get_value() * 1.E6, 2)
        div = math.pow(10, 2)

        mul = 0
        while val >= div:
            val //= 10
            mul += 1

            if val < div and round(val) != val:
                val = round(val)

        if val < math.pow(10, 0):
            val *= 100
            mul = 11
        elif val < math.pow(10, 1):
            val *= 10
            mul = 10

        val = str(round(val)).ljust(1, "0")
        result = list(map(lambda v: int(v), list(val)))
        result.append(mul)

        return result
