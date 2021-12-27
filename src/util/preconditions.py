def check_value(condition, message):
    if not condition:
        raise ValueError(message)
