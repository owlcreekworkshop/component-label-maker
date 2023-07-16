import math

SI_STR_EXP_MAP = {
    "E": 18,
    "P": 15,
    "T": 12,
    "G": 9,
    "M": 6,
    "k": 3,
    "": 0,
    "m": -3,
    "u": -6,
    "\u03BC": -6,
    "n": -9,
    "p": -12,
    "f": -15,
    "a": -18,
}

SI_EXP_STR_MAP = {
    18: "E",
    15: "P",
    12: "T",
    9: "G",
    6: "M",
    3: "k",
    0: "",
    -3: "m",
    -6: "\u03BC",
    -9: "n",
    -12: "p",
    -15: "f",
    -18: "a",
}


class ComponentValue:
    def __init__(self, value: float):
        self.set_value(value)

    def __str__(self) -> str:
        return self.get_value_formatted()

    def get_value(self, suffix: str = None) -> float:
        if suffix is not None:
            exp = self._get_exp_for_suffix(suffix)
            return self.raw / math.pow(10, exp)
        else:
            return self.raw

    def get_value_formatted(self, suffix: str = None, places: int = 2) -> str:
        if suffix is not None:
            exp = self._get_exp_for_suffix(suffix)
        else:
            exp = self.get_exp()

        value = round(self.raw / math.pow(10, exp), places)
        prefix = SI_EXP_STR_MAP.get(exp)

        return f"{value:,g}{prefix}"

    def get_exp(self) -> int:
        exp = math.log10(self.raw)

        for i in SI_EXP_STR_MAP.keys():
            if exp >= i:
                exp = i
                break

        return exp

    def set_value(self, value: any):
        if isinstance(value, float) or isinstance(value, int):
            value = self._set_value_float(value)
        else:
            self._set_value_str(value)

    def _set_value_float(self, value: float):
        self.raw = value

    def _set_value_str(self, value: str):
        unit = value.strip()[-1:]
        if unit in SI_STR_EXP_MAP.keys():
            value = float(value.strip()[:-1])
            scale = SI_STR_EXP_MAP.get(unit)
        else:
            value = float(value.strip())
            scale = 0

        v = value * math.pow(10, scale)

        self._set_value_float(v)

    def _get_exp_for_suffix(self, suffix: str) -> int:
        return SI_STR_EXP_MAP.get(suffix)

    def _get_suffix_for_exp(self, exp: int) -> str:
        return SI_EXP_STR_MAP.get(exp)
