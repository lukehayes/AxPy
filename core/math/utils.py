#- Math Utility Functions  -------------------------------------------------#

def lerp(value, start, end):
    """
    Linearly interpolate between two values.

    Args:
        value (int): The initial value
        start (int): The starting value
        end   (int): The ending value

    Returns:
        Float: Linear interpolation between start and end.
    """
    return (value - start) * (
        1 / (end - start)
    )


