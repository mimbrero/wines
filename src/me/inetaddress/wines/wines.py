import csv
from collections import namedtuple
from datetime import date
from statistics import mean
from typing import List, Iterable, Callable

from me.inetaddress.wines.util.parsing_utils import parse_date

# --------------------------------------
# ENTREGA 1
# --------------------------------------
Wine = namedtuple("Wine", "name, country, region, winery, rating, number_of_ratings, price, since, origin_appellation")


def parse_file(path: str) -> List[Wine]:
    """
    Abre el archivo que se sitúa en la ruta dada como parámetro y lo parsea en una lista de tuplas de tipo Wine.
    El archivo debe estar codificado en utf-8.

    @param path: la ruta del archivo a parsear
    @return una lista de tuplas de tipo Wine con los valores del archivo
    """
    with open(path, encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Pasamos la línea 0, que solo es la cabecera con la descripción de las columnas

        to_return = []
        for name, country, region, winery, rating, number_of_ratings, price, since, origin_appellation in reader:
            wine = Wine(name, country, region, winery, float(rating), int(number_of_ratings), float(price),
                        parse_date(since), bool(origin_appellation))
            to_return.append(wine)

        return to_return


# --------------------------------------
# ENTREGA 2
# --------------------------------------

# Bloque I
today: date = date.today()  # Constant to prevent constructing every time


def calculate_age(wine: Wine, from_date: date = today) -> float:
    """
    Calcula la edad del vino dado, en años, con decimales redondeados a 2 cifras.

    @param wine: vino a calcular la edad
    @param from_date: fecha para calcular la edad (por defecto hoy)
    @return: la edad del vino, en años
    """
    return round((from_date - wine.since).days / 365, 2)


def filter_by_age(wines: Iterable[Wine], min_age: float, from_date: date = today) -> List[Wine]:
    """
    Filtra por edad mínima el Iterable de Wines pasado como argumento.

    @param wines: Iterable de Wines a filtrar
    @param min_age: edad mínima que deben tener los vinos
    @param from_date: fecha para calcular la edad (por defecto hoy)
    @return: un Iterable de Wines ya filtrado por edad mínima
    """
    return list(filter(lambda wine: calculate_age(wine, from_date) >= min_age, wines))


def calculate_mean_age(wines: Iterable[Wine], from_date: date = today) -> float:
    """
    Calcula la media de edad de los vinos que contiene el Iterable pasado como argumento.

    @param wines: Iterable de Wines a calcular la media
    @param from_date: fecha para calcular la edad (por defecto hoy)
    @return: la media de edad de los vinos
    """
    return mean(calculate_age(wine, from_date) for wine in wines)
