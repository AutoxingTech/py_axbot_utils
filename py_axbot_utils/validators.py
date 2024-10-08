from .exceptions import ValidationError
from .translations import _


class RangeValidator:
    def __init__(self, min_value, max_value) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if self.min_value and value < self.min_value:
            raise ValidationError(
                _("Value {} should not be smaller than{}").format(self.min_value)
            )

        if self.max_value and value > self.max_value:
            raise ValidationError(
                _("Value {} should not be larger than{}").format(self.max_value)
            )
