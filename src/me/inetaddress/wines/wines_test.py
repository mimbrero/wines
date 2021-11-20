from me.inetaddress.wines import wines
from me.inetaddress.wines.util.test_utils import *
from me.inetaddress.wines.wines import Wine


def main():
    dataset_path = "../../../../data/wine_data.csv"

    # Entrega 1
    test_parse_file(dataset_path)

    data = wines.parse_file(dataset_path)

    # Entrega 2
    test_filter_by_country(data)
    test_calculate_mean_age(data)
    test_get_oldest_wines(data)


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
    print_iterable(wines.filter_by_country(data, country))


def test_calculate_mean_age(data: Sequence[Wine]) -> None:
    print_test_header("calculate_mean_age")
    print("La edad media de los vinos dados es de", wines.calculate_mean_age(data), "años")


# ----------
# BLOQUE II
# ----------
def test_get_oldest_wines(data: Sequence[Wine]) -> None:
    print_test_header("get_oldest_wines")
    print("El/los vino/s más antiguos es/son:")
    print_iterable(wines.get_oldest_wines(data))


if __name__ == "__main__":
    main()
