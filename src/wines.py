import csv
from collections import namedtuple, defaultdict, Counter
from datetime import date
from statistics import mean
from typing import List, Iterable, Dict, Tuple

from util import preconditions
from util.parsing_utils import parse_date, parse_bool

Wine = namedtuple("Wine", "name, country, region, winery, rating, number_of_ratings, price, since, origin_appellation")
today = date.today()  # Constant to prevent constructing every time


# ----------------------------------------------------------------------------------------------------------------------
#                                                     ENTREGA 1
# ----------------------------------------------------------------------------------------------------------------------

def parse_csv_file(path: str) -> List[Wine]:
    """
    Abre el archivo que se sitúa en la ruta dada como parámetro y lo parsea en una lista de Wines.
    El archivo debe estar codificado en utf-8.

    @param path: la ruta del archivo a parsear
    @return: una lista con los valores del archivo ya parseados a objetos Wine.
    """
    with open(path, mode="rt", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Pasamos la línea 0, que solo es la cabecera con la descripción de las columnas

        to_return = []
        for name, country, region, winery, rating, number_of_ratings, price, since, origin_appellation in reader:
            wine = Wine(name, country, region, winery,
                        float(rating),
                        int(number_of_ratings),
                        float(price),
                        parse_date(since),
                        parse_bool(origin_appellation)
                        )
            to_return.append(wine)

        return to_return


# ----------------------------------------------------------------------------------------------------------------------
#                                                     ENTREGA 2
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
#                                                     BLOQUE I
# ----------------------------------------------------------------------------------------------------------------------

# 1) Función que filtre y/o seleccione una serie de filas y/o columnas del dataset
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

    Funcionamiento: primero calcula el timedelta entre el parámetro from_date y la fecha del vino. Luego convierte a
    días ese timedelta, y lo divide entre 365. La salida está redondeada a 2 decimales.

    @param wine: vino a calcular la edad
    @param from_date: fecha para calcular la edad (por defecto hoy)
    @return: la edad del vino, en años
    """
    preconditions.check_value(from_date <= today, "The from_date parameter must be before or the same as date.today()")
    return round((from_date - wine.since).days / 365, 2)


# 3) Función que calcule la suma, el total o la media de una propiedad numérica.
#
# NOTA: La propiedad numérica está calculada en este caso. Como el dataset no tiene una columna de "edad",
# la calculamos con la función #calculate_age, que lo hace por el atributo "since" del vino, de tipo date.
def calculate_mean_age(wines: Iterable[Wine], from_date: date = today) -> float:
    """
    Calcula la media de edad de los Wines que contiene el Iterable pasado como argumento.

    Funcionamiento: primero crea un Iterable con la edad de cada vino y posteriormente hace la media de ese Iterable.
    · Mirar #calculate_age para más información sobre el cálculo de edad.

    @param wines: Iterable de Wines a calcular la media
    @param from_date: fecha para calcular la edad (por defecto hoy)
    @return: la media de edad de los vinos
    """
    return mean(calculate_age(wine, from_date) for wine in wines)


# ----------------------------------------------------------------------------------------------------------------------
#                                                    BLOQUE II
# ----------------------------------------------------------------------------------------------------------------------

# 5) Función que obtenga una lista con las tuplas cuyo valor de una propiedad concreta es igual al máximo o mínimo
# valor de esa propiedad.
def get_oldest_wines(wines: Iterable[Wine]) -> List[Wine]:
    """
    Obtiene una lista con los vinos que tengan la fecha más antigua del Iterable de Wines pasado como argumento.

    Funcionamiento: primero calcula la fecha más antigua entre todos los vinos del Iterable pasado como argumento.
    Posteriormente, retorna una lista con los vinos que tengan esa fecha. Probablemente sea solo uno.

    @param wines: Iterable de Wines a obtener el más viejo
    @return: una lista con los vinos más antiguos del Iterable
    """
    oldest_date = min(wine.since for wine in wines)
    return [wine for wine in wines if wine.since == oldest_date]


# 6) Función que obtenga una lista con n tuplas ordenadas de mayor a menor (o de menor a mayor) por una
# propiedad determinada de entre las que cumplan una condición.
def sort_by_age(wines: Iterable[Wine], descendant: bool = False, min_age: float = -1, limit: int = -1,
                from_date: date = today) -> List[Wine]:
    """
    Obtiene una lista ordenada por edad a partir del Iterable de Wines dado como parámetro.

    Funcionamiento: primero crea una lista a partir del Iterable pasado como argumento solo con los vinos cuya edad
    sea mayor al parámetro min_age. Posteriormente, ordena la lista por fecha en orden descendente, y la retorna.

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


# 7) Función que devuelva un diccionario que permita agrupar por una propiedad, en el que los valores sean una
# lista o un conjunto con las tuplas que tienen el mismo valor de esa propiedad.
def group_by_ratings(wines: Iterable[Wine], just_ints: bool = False) -> Dict[float, List[Wine]]:
    """
    Dado un Iterable de Wines, devuelve un diccionario en el que las claves representan una valoración, y el valor es
    una lista con los vinos que tienen esa valoración.

    Funcionamiento: primero crea un defaultdict cuya factory es la función list. Luego, añade cada vino del Iterable
    pasado como argumento a la lista del diccionario cuya clave es la valoración del vino. La clave será su
    valoración exacta si el parámetro just_ints es False, o su valoración truncada si just_ints es True.

    @param wines: vinos a agrupar por valoración
    @param just_ints: True si solo se quiere agrupar en valoraciones sin decimales. Un vino con valoración 3.6 se
    agrupará con los de valoración 3
    @return: un diccionario con clave float y valor List[Wine], ya explicado anteriormente
    """
    grouped: Dict[float, List[Wine]] = defaultdict(list)

    for wine in wines:
        rating: float = int(wine.rating) if just_ints else wine.rating
        grouped[rating].append(wine)

    return grouped


# ----------------------------------------------------------------------------------------------------------------------
#                                                     ENTREGA 3
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
#                                                    BLOQUE III
# ----------------------------------------------------------------------------------------------------------------------

# 1) Función que devuelva un diccionario que hace corresponder a cada clave el número de tuplas que contienen
# dicha clave.
def count_wines_per_country(wines: Iterable[Wine], min_rating: float = -1, min_price: float = -1) -> Counter[str, int]:
    """
    Dado un Iterable de Wines, devuelve un Diccionario (Counter específicamente) cuyas clave son países y los valores
    son el número de vinos de ese país, que tienen como mínimo una valoración min_rating y precio min_price (parámetros
    que por defecto son -1).

    Funcionamiento: crea un Counter a partir de un Iterable por comprensión que contiene los países del Iterable pasado
    como argumento, cada vez que el elemento tenga valoración y precio mayor o igual a los parámetros min_rating y
    min_price.

    @param wines: vinos a obtener los valores del Counter
    @param min_rating: valoración mínima que debe tener un vino para ser contado
    @param min_price: precio mínimo que debe tener un vino para ser contado
    @return: un Counter con claves str y valores int, ya explicado anteriormente
    """
    return Counter(wine.country for wine in wines if wine.rating >= min_rating and wine.price >= min_price)


# 3) Función que devuelva un máximo o mínimo a partir de un diccionario que hace corresponder a cada clave el número
# de tuplas que contienen dicha clave.
def get_most_wine_producing_country(frequency: Dict[str, int]) -> Tuple[str, int]:
    """
    Dado un diccionario donde las claves son países y los valores son el número de vinos de ese país, devuelve una
    tupla con el país que más vinos produce y el número de vinos que produce en ese orden.

    Funcionamiento: si el diccionario dado como parámetro no es de tipo Counter, instancia uno a partir del diccionario.
    Si lo es, continúa. Luego, mediante Counter#most_common, obtiene la primera tupla clave-valor.

    @param frequency: diccionario, preferiblemente un Counter, donde las claves son países y los valores son el
    número de vinos de ese país
    @return: una tupla con una str y un int en ese orden, explicado anteriormente
    """
    if not isinstance(frequency, Counter):
        frequency = Counter(frequency)

    return frequency.most_common(1)[0]


# 6) Función que devuelva un diccionario que hace corresponder a cada clave el porcentaje de alguna propiedad de las
# tuplas que contienen dicha clave respecto al total de tuplas
def get_percentages_of_origin_appellations_by_country(wines: Iterable[Wine]) -> Dict[str, float]:
    """
    Dado un Iterable de Wines, devuelve un diccionario cuyas claves son países y los valores son el porcentaje de
    vinos producidos en ese país que tienen denominación de origen frente al total de vinos con denominación de origen.

    Funcionamiento: primero recorre el Iterable de Wines para contar el total de vinos que tienen la propiedad
    origin_appellation como True, y los agrupa en un diccionario cuyas claves son países y los valores son el número
    de vinos de ese país que tienen la propiedad origin_appellation como True. Posteriormente recorre los items de
    ese diccionario y genera otro calculando el porcentaje explicado anteriormente.

    @param wines: vinos a calcular los porcentajes
    @return: un diccionario con claves str y valores float, explicado anteriormente
    """
    # NOTE: Not reusing the #count_wines_per_country function because this implementation manages to iterate just
    # 2 times the data.

    total_origin_appellations = 0
    counter = defaultdict(int)

    for wine in wines:
        if not wine.origin_appellation:
            continue

        total_origin_appellations += 1
        counter[wine.country] += 1

    # Now that we have collected the needed data, return the percentages instead of the count.

    return {country: count / total_origin_appellations for country, count in counter.items()}


# 7) Función que devuelva un diccionario que hace corresponder a cada clave una lista ordenada con los n mayores o
# menores elementos que contienen dicha clave.
def group_by_country_sorted_by_rating(wines: Iterable[Wine], n: int = 10,
                                      descendant: bool = False) -> Dict[str, List[Wine]]:
    """
    Dado un Iterable de Wines, devuelve un diccionario cuyas claves son países y los valores son una lista de n vinos
    de ese país ordenada de menor a mayor (o de mayor a menor si descendant es True) valoración.

    Funcionamiento: primero crea un diccionario que agrupa los vinos por país, y posteriormente ordena los valores de
    ese diccionario por valoración del vino (en orden descendente si lo pide el parámetro descendant), haciendo slice
    a n elementos.

    @param wines: vinos a agrupar por país ordenados por valoración
    @param n: número máximo de vinos que contendrán los valores del diccionario
    @param descendant: True si se deben ordenar de mejor a menor valoración (por defecto False)
    @return: un diccionario con claves str y valores List[Wine], explicado anteriormente
    """
    preconditions.check_value(n > 0, "n parameter must be > 0")

    grouped = defaultdict(list)
    for wine in wines:
        grouped[wine.country].append(wine)

    return {
        country: sorted(wine_list, key=lambda wine: wine.rating, reverse=descendant)[:n]
        for country, wine_list in grouped.items()
    }

    return grouped
