from typing import Dict, List

import wines
from util.test_utils import *
from wines import Wine


def main():
    dataset_path = "../data/wine_data.csv"

    # Entrega 1
    test_parse_file(dataset_path)

    # Now that we just tested the parse_file function, we can use it and save the data to not parse every time.
    data = wines.parse_csv_file(dataset_path)

    # Entrega 2
    test_filter_by_country(data)
    test_calculate_mean_age(data)
    test_get_oldest_wines(data)
    test_sort_by_age(data)
    test_group_by_ratings(data)

    # Entrega 3
    test_count_wines_per_country(data)
    test_get_most_wine_producing_country(data)
    test_get_percentages_of_origin_appellations_by_country(data)
    test_group_by_country_sorted_by_rating(data)

    # Entrega 4
    test_generate_wines_per_country_pie_chart(data)


# ----------------------------------------------------------------------------------------------------------------------
#                                                     ENTREGA 1
# ----------------------------------------------------------------------------------------------------------------------

def test_parse_file(path: str) -> None:
    print_test_header("parse_file")
    wine_list = wines.parse_csv_file(path)
    print("Leídos", len(wine_list), "vinos")

    print("3 primeros vinos leídos:")
    for wine in wine_list[:3]:
        print(" -", wine)

    print("3 últimos vinos leídos:")
    for wine in wine_list[-3:]:
        print(" -", wine)


# ----------------------------------------------------------------------------------------------------------------------
#                                                     ENTREGA 2
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
#                                                     BLOQUE I
# ----------------------------------------------------------------------------------------------------------------------
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


# ----------------------------------------------------------------------------------------------------------------------
#                                                     BLOQUE II
# ----------------------------------------------------------------------------------------------------------------------
def test_get_oldest_wines(data: Sequence[Wine]) -> None:
    print_test_header("get_oldest_wines")
    print("El vino más antiguo es:")
    print_iterable(wines.get_oldest_wines(data))


def test_sort_by_age(data: Sequence[Wine]) -> None:
    print_test_header("sort_by_age")

    print("Los 5 vinos más antiguos son:")
    print_sequence(wines.sort_by_age(data, limit=5), offset=1)

    print("\nMientras que los más 5 más nuevos son:")
    print_sequence(wines.sort_by_age(data, descendant=True, limit=5), offset=1)

    print("\nY los más 2 más nuevos con al menos 5 años son:")
    print_sequence(wines.sort_by_age(data, min_age=5, descendant=True, limit=2), offset=1)


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


# ----------------------------------------------------------------------------------------------------------------------
#                                                     ENTREGA 3
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
#                                                    BLOQUE III
# ----------------------------------------------------------------------------------------------------------------------
def test_count_wines_per_country(data: Sequence[Wine]):
    print_test_header("count_wines_per_country")
    count = wines.count_wines_per_country(data)
    print("Eslovenia produce", count["Slovenia"], "vinos")
    print("Eslovaquia produce", count["Slovakia"], "vinos")

    print("Italia produce", wines.count_wines_per_country(data, min_rating=3.5)["Italy"],
          "vinos con una valoración mayor o igual a 3.5.")

    print("Italia produce", wines.count_wines_per_country(data, min_rating=4.5)["Italy"],
          "vinos con una valoración mayor o igual a 4.5.")


def test_get_most_wine_producing_country(data: Sequence[Wine]):
    print_test_header("get_most_wine_producing_country")
    country, count = wines.get_most_wine_producing_country(wines.count_wines_per_country(data))
    print("El país que más vinos produce es", country, "con", count, "vinos.")


def test_get_percentages_of_origin_appellations_by_country(data: Sequence[Wine]):
    print_test_header("get_percentages_of_origin_appellations_by_country")
    percentages = wines.get_percentages_of_origin_appellations_by_country(data)

    print(f"El porcentaje de vinos con denominación de origen de Italia sobre el total es de "
          f"{percentages['Italy'] * 100}%")
    print(f"El porcentaje de vinos con denominación de origen de Eslovenia sobre el total es de "
          f"{percentages['Slovenia'] * 100}%")
    print(f"El porcentaje de vinos con denominación de origen de Portugal sobre el total es de "
          f"{percentages['Portugal'] * 100}%")


def test_group_by_country_sorted_by_rating(data: Sequence[Wine]):
    print_test_header("group_by_country_sorted_by_rating")
    best = wines.group_by_country_sorted_by_rating(data, n=5, descendant=True)
    worst = wines.group_by_country_sorted_by_rating(data, n=5)

    print(f"Los 5 mejores vinos de Italia son:")
    print_sequence(best["Italy"], offset=1)

    print(f"Mientras que los 5 peores vinos de Italia son:")
    print_sequence(worst["Italy"], offset=1)


# ----------------------------------------------------------------------------------------------------------------------
#                                                     BLOQUE IV
# ----------------------------------------------------------------------------------------------------------------------
def test_generate_wines_per_country_pie_chart(data: Sequence[Wine]):
    print_test_header("generate_wines_per_country_pie_chart")
    print("Generando un gráfico circular que representa el porcentaje que tiene cada país del total de los vinos...")
    wines.generate_wines_per_country_pie_chart(data)


if __name__ == "__main__":
    main()
