import csv
from collections import namedtuple, defaultdict, Counter
from datetime import date
from statistics import mean
from typing import List, Iterable, Dict

from util.parsing_utils import parse_date

# --------------------------------------
# ENTREGA 1
# --------------------------------------
Wine = namedtuple("Wine", "name, country, region, winery, rating, number_of_ratings, price, since, origin_appellation")


def parse_file(path: str) -> List[Wine]:
    """
    Abre el archivo que se sitúa en la ruta dada como parámetro y lo parsea en una lista de tuplas de tipo Wine.
    El archivo debe estar codificado en utf-8.

    @param path: la ruta del archivo a parsear
    @return: una lista con los valores del archivo ya parseados a objetos Wine.
    """
    with open(path, encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Pasamos la línea 0, que solo es la cabecera con la descripción de las columnas

        to_return = []
        for name, country, region, winery, rating, number_of_ratings, price, since, origin_appellation in reader:
            wine = Wine(name, country, region, winery, float(rating), int(number_of_ratings), float(price),
                        parse_date(since), eval(origin_appellation.capitalize()))
            to_return.append(wine)

        return to_return


# --------------------------------------
# ENTREGA 2
# --------------------------------------

# ----------
# BLOQUE I
# ----------
today: date = date.today()  # Constant to prevent constructing every time


# Se pide: Función que filtre y/o seleccione una serie de filas y/o columnas del dataset
def filter_by_country(wines: Iterable[Wine], country: str) -> List[Wine]:
    """
    Filtra por país el Iterable de Wines dado como parámetro.

    @param wines: Iterable de Wines a filtrar
    @param country: país para filtrar el Iterable
    @return: una lista ya filtrada con los vinos que pertenecen al país dado
    """
    return [wine for wine in wines if wine.country == country]


# !) Función útil para calcular la edad de un vino. No forma parte del bloque ni de la entrega realmente.
def calculate_age(wine: Wine, from_date: date = today) -> float:
    """
    Calcula la edad del vino dado, en años, con decimales redondeados a 2 cifras.

    Primero calcula el timedelta entre el parámetro from_date y la fecha del vino. Luego convierte a días ese
    timedelta, y lo divide entre 365. La salida está redondeada a 2 decimales.

    @param wine: vino a calcular la edad
    @param from_date: fecha para calcular la edad (por defecto hoy)
    @return: la edad del vino, en años
    """
    return round((from_date - wine.since).days / 365, 2)


# Se pide: Función que calcule la suma, el total o la media de una propiedad numérica.
# La propiedad numérica está calculada en este caso. Como el dataset no tiene una columna de "edad", la calculamos con
# la función #calculate_age, que lo hace por el atributo "since" del vino, de tipo date.
def calculate_mean_age(wines: Iterable[Wine], from_date: date = today) -> float:
    """
    Calcula la media de edad de los Wines que contiene el Iterable pasado como argumento.

    Primero crea un Iterable con la edad de cada vino y posteriormente hace la media de ese Iterable.
    · Mirar #calculate_age para más información sobre el cálculo de edad.

    @param wines: Iterable de Wines a calcular la media
    @param from_date: fecha para calcular la edad (por defecto hoy)
    @return: la media de edad de los vinos
    """
    return mean(calculate_age(wine, from_date) for wine in wines)


# ----------
# BLOQUE II
# ----------
# Se pide: Función que obtenga una lista con las tuplas cuyo valor de una propiedad concreta es igual al máximo o mínimo
# valor de esa propiedad.
def get_oldest_wines(wines: Iterable[Wine]) -> List[Wine]:
    """
    Obtiene una lista con los vinos que tengan la fecha más antigua del Iterable de Wines pasado como argumento.

    Primero calcula la fecha más antigua entre todos los vinos del Iterable pasado como argumento.
    Posteriormente, retorna una lista con los vinos que tengan esa fecha. Probablemente sea solo uno.

    @param wines: Iterable de Wines a obtener el más viejo
    @return: una lista con los vinos más antiguos del Iterable
    """
    oldest_date = min(wine.since for wine in wines)
    return [wine for wine in wines if wine.since == oldest_date]


# Se pide: Función que obtenga una lista con n tuplas ordenadas de mayor a menor (o de menor a mayor) por una
# propiedad determinada de entre las que cumplan una condición.
def sort_by_age(
        wines: Iterable[Wine],
        descendant: bool = False,
        min_age: float = 0,
        limit: int = -1,
        from_date: date = today
) -> List[Wine]:
    """
    Obtiene una lista ordenada por edad a partir del Iterable de Wines dado como parámetro.

    Primero crea una lista a partir del Iterable pasado como argumento solo con los vinos cuya edad sea mayor al
    parámetro min_age. Posteriormente, ordena la lista por fecha en orden descendente, y la retorna.

    @param wines: Iterable de Wines a obtener la lista ordenada
    @param descendant: True si se deben ordenar de más nuevo a más viejo (por defecto False)
    @param min_age: edad mínima que deben tener los vinos
    @param limit: límite para la lista devuelta. Si es menor que 1, no tendrá límite.
    @param from_date: fecha para calcular la edad (por defecto hoy)
    @return: una lista de vinos ordenada por edad
    """
    filtered = [wine for wine in wines if calculate_age(wine, from_date) >= min_age]
    filtered.sort(key=lambda wine: wine.since, reverse=descendant)

    if limit > 0:
        filtered = filtered[:limit]

    return filtered


# Se pide: Función que devuelva un diccionario que permita agrupar por una propiedad, en el que los valores sean una
# lista o un conjunto con las tuplas que tienen el mismo valor de esa propiedad.
def group_by_ratings(wines: Iterable[Wine], just_ints: bool = False) -> Dict[float, List[Wine]]:
    """
    Dado un Iterable de Wines, devuelve un diccionario en el que las claves representan una valoración, y el valor es
    una lista con los vinos que tienen esa valoración.

    Primero crea un defaultdict cuya factory es la función list. Luego, añade cada vino del Iterable pasado como
    argumento a la lista del diccionario cuya clave es la valoración del vino. La clave será su valoración
    exacta si el parámetro just_ints es False, o su valoración truncada si just_ints es True.

    @param wines: vinos a agrupar por valoración
    @param just_ints: True si solo se quiere agrupar en valoraciones sin decimales. Un vino con valoración 3.6 se
    agrupará con los de valoración 3

    @return: un diccionario agrupando los vinos por valoración
    """
    grouped: Dict[float, List[Wine]] = defaultdict(list)

    for wine in wines:
        rating: float = int(wine.rating) if just_ints else wine.rating
        grouped[rating].append(wine)

    return grouped


# --------------------------------------
# ENTREGA 3
# --------------------------------------

# ----------
# BLOQUE III
# ----------
# Se pide: Función que devuelva un diccionario que hace corresponder a cada clave el número de tuplas que contienen
# dicha clave.
def count_wines_per_country(
        wines: Iterable[Wine],
        min_rating: float = -1,
        min_price: float = -1
) -> Counter[str, int]:
    return Counter(wine.country for wine in wines if wine.rating >= min_rating and wine.price >= min_price)

