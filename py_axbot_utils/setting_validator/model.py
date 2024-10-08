validator_map = {}


def validator(name: str):
    """
    Function style validator of a variable

    A validator function should accept variable value as the only input param,
    Raise a ValueError exception when some error is found.

    Here is an example:

    @validator("robot.footprint")
    def validate_robot_footprint(footprint):
        if not instance(footprint, list):
            raise ValueError("Footprint must be an array")
    """

    def decorator(func):
        validator_map[name] = func
        return func

    return decorator
