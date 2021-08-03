#- Math Utility Functions  -------------------------------------------------#

def lerp(value, start, end):
    return (value - start) * (
        1 / (end - start)
    )

