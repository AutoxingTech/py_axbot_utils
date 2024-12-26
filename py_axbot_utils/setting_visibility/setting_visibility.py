visibility_map = {}


def visibility(name: str):
    """
    Visibility of a variable

    A visible function should accept variable value as the only input param.
    Return True if visible, and False if not visible or some error is found.

    Here is an example:

    @visibility("robot.footprint")
    def is_robot_footprint_visible(footprint):
        if not instance(footprint, list):
            return False
    """

    def decorator(func):
        visibility_map[name] = func
        return func

    return decorator


def is_visible(var_name: str, value):
    """
    Return True if visible, and False if not visible or some error is found.
    """
    visible_func = visibility_map.get(var_name)
    if visible_func:
        visible_func(value)
