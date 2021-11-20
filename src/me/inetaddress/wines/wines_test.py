from me.inetaddress.wines import wines
from me.inetaddress.wines.util.test_utils import *
from me.inetaddress.wines.wines import Wine


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

# Bloque I
def test_filter_by_age(data: Iterable[Wine]) -> None:
    print_test_header("filter_by_age")
    filter_by_age_and_print(data, 22)
    filter_by_age_and_print(data, 22.8)
    filter_by_age_and_print(data, 800)


def filter_by_age_and_print(data: Iterable[Wine], min_age: float) -> None:
    print("\nVinos con más de", min_age, "años")
    print_sequence(wines.filter_by_age(data, min_age))


# Bloque II
# TODO


def main():
    dataset_path = "../../../../data/wine_data.csv"
    test_parse_file(dataset_path)

    data = wines.parse_file(dataset_path)
    test_filter_by_age(data)


if __name__ == "__main__":
    main()
