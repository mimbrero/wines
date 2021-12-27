def check_value(condition, message):
    """
    Raises a ValueError with the given message if the given condition is not True.

    @param condition: condition to check if it's True
    @param message: message to raise the ValueError
    """
    if not condition:
        raise ValueError(message)
