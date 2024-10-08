from .validators import RangeValidator


class Field:
    def __init__(self, name, default=None) -> None:
        self.name = name
        self.default = default
        self.validators = []


class NumberField(Field):
    def __init__(self, name, min_value=None, max_value=None, default=None) -> None:
        super().__init__(name, default)

        self.validators.append(RangeValidator(min_value, max_value))
