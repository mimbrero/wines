from typing import Dict, List

import wines
from wines import Wine
from util.test_utils import *


def main():
    dataset_path = "../data/wine_data.csv"

    # Entrega 1
    test_parse_file(dataset_path)

    # Ahora que hemos probado la función parse_file, podemos guardar su resultado para no parsear múltiples veces.
    data = wines.parse_file(dataset_path)

    # Entrega 2
    test_filter_by_country(data)
    test_calculate_mean_age(data)
    test_get_oldest_wines(data)
    test_sort_by_age(data)
    test_group_by_ratings(data)


# --------------------------------------
# ENTREGA 1
# --------------------------------------

def test_parse_file(path: str) -> None:
    print_test_header("parse_file")
    wine_list = wines.parse_file(path)
    print("Leídos", len(wine_list), "vinos")

    print("3 primeros vinos leídos:")
    for wine in wine_list[:3]:
        print(" -", wine)

    print("3 últimos vinos leídos:")
    for wine in wine_list[-3:]:
        print(" -", wine)


# --------------------------------------
# ENTREGA 2
# --------------------------------------

# ----------
# BLOQUE I
# ----------
def test_filter_by_country(data: Sequence[Wine]) -> None:
    print_test_header("filter_by_country")
    filter_by_country_and_print(data, "Portugal")
    filter_by_country_and_print(data, "Israel")
    filter_by_country_and_print(data, "ThisCountryDoesNotExist")


def filter_by_country_and_print(data: Sequence[Wine], country: str) -> None:
    print(f"\nVinos de {country}:")
    print_sequence(wines.filter_by_country(data, country))


def test_calculate_mean_age(data: Sequence[Wine]) -> None:
    print_test_header("calculate_mean_age")
    print("La edad media de los vinos dados es de", wines.calculate_mean_age(data), "años")


# ----------
# BLOQUE II
# ----------
def test_get_oldest_wines(data: Sequence[Wine]) -> None:
    print_test_header("get_oldest_wines")
    print("El vino más antiguo es:")
    print_iterable(wines.get_oldest_wines(data))


def test_sort_by_age(data: Sequence[Wine]) -> None:
    print_test_header("sort_by_age")

    print("Los 5 vinos más antiguos son:")
    print_sequence(wines.sort_by_age(data, limit=5))

    print("\nMientras que los más 5 más nuevos son:")
    print_sequence(wines.sort_by_age(data, descendant=True, limit=5))

    print("\nY los más 2 más nuevos con al menos 5 años son:")
    print_sequence(wines.sort_by_age(data, min_age=5, descendant=True, limit=2))


def test_group_by_ratings(data: Sequence[Wine]) -> None:
    print_test_header("group_by_ratings")

    print("\nPara puntuaciones con decimales:")
    grouped = wines.group_by_ratings(data)
    print_rated(grouped, 4.6)
    print_rated(grouped, 4.8)

    print("\n\nPara puntuaciones del 0-5 sin decimales:")
    grouped = wines.group_by_ratings(data, just_ints=True)
    print_rated(grouped, 2)


def print_rated(grouped: Dict[float, List[Wine]], rate: float) -> None:
    print("\nLos vinos con una puntuación de", rate, "son:")
    print_iterable(grouped[rate])


if __name__ == "__main__":
    main()
