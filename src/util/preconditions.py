def check_value(condition, message):
    """
    Levanta un ValueError con el mensaje especificado en el parámetro message si condition no es True.

    @param condition: condition to check if it's True
    @param message: message to raise the ValueError
    """
    if not condition:
        raise ValueError(message)
