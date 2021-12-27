from datetime import datetime, date


def parse_bool(to_parse: str) -> bool:
    """
    Parsea un bool dado en tipo str.

    @param to_parse: bool a parsear
    @return bool parseado
    """
    return eval(to_parse.capitalize())


def parse_date(to_parse: str) -> date:
    """
    Parsea una fecha dada en tipo str con formato dd/mm/aaaa.

    @param to_parse: fecha a parsear
    @return fecha parseada
    """
    return datetime.strptime(to_parse, "%d/%m/%Y").date()
