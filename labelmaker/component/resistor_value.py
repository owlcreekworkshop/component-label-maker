import math

from labelmaker.component.component_value import ComponentValue


class ResistorValue():
    def __init__(self, value: ComponentValue):
        if isinstance(value, ComponentValue):
            self.decorated = value
        else:
            self.decorated = ComponentValue(value)

    def __str__(self) -> str:
        return self.decorated.__str__() + "\u2126"

    def get_value(self, suffix: str = None) -> float:
        return self.decorated.get_value(suffix)

    def get_value_formatted(self, suffix: str = None) -> str:
        return self.decorated.get_value_formatted(suffix) + "\u2126"

    def get_exp(self) -> float:
        return self.decorated.get_exp()

    def set_value(self, value: any):
        self.decorated.set_value(value)

    def get_color_bands(self, bands: 3):
        val = self.get_value()
        div = math.pow(10, bands - 1)

        mul = 0
        while val >= div:
            val //= 10
            mul += 1

            if val < div and round(val) != val:
                val = round(val)

        if val < math.pow(10, bands - 3):
            val *= 100
            mul = 11
        elif val < math.pow(10, bands - 2):
            val *= 10
            mul = 10

        val = str(round(val)).ljust(bands - 1, "0")
        result = list(map(lambda v: int(v), list(val)))
        result.append(mul)

        return result
