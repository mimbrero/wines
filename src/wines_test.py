from abc import abstractmethod, ABC
from typing import Dict, List, Sequence

import wines
from util.test_utils import print_test_header, print_iterable, print_sequence
from wines import Wine


class WinesTest(ABC):
    @abstractmethod
    def __init__(self, data: Sequence[Wine]):
        self.data = data

    # --------------------------------------
    # ENTREGA 1
    # --------------------------------------
    def test_parse_file(self):
        print_test_header("parse_file")
        print("Leídos", len(self.data), "vinos")

        print("3 primeros vinos leídos:")
        print_sequence(self.data[:3])

        print("3 últimos vinos leídos:")
        print_sequence(self.data[-3:])

    # --------------------------------------
    # ENTREGA 2
    # --------------------------------------

    # ----------
    # BLOQUE I
    # ----------
    def test_filter_by_country(self):
        print_test_header("filter_by_country")
        self._filter_by_country_and_print(self.data, "Portugal")
        self._filter_by_country_and_print(self.data, "Israel")
        self._filter_by_country_and_print(self.data, "ThisCountryDoesNotExist")

    @staticmethod
    def _filter_by_country_and_print(data: Sequence[Wine], country: str):
        print(f"\nVinos de {country}:")
        print_iterable(wines.filter_by_country(data, country))

    def test_calculate_mean_age(self):
        print_test_header("calculate_mean_age")
        print("La edad media de los vinos dados es de", wines.calculate_mean_age(self.data), "años")

    # ----------
    # BLOQUE II
    # ----------
    def test_get_oldest_wines(self):
        print_test_header("get_oldest_wines")
        print("El vino más antiguo es:")
        print_iterable(wines.get_oldest_wines(self.data))

    def test_sort_by_age(self):
        print_test_header("sort_by_age")

        print("Los 5 vinos más antiguos son:")
        print_sequence(wines.sort_by_age(self.data, limit=5))

        print("\nMientras que los más 5 más nuevos son:")
        print_sequence(wines.sort_by_age(self.data, descendant=True, limit=5))

        print("\nY los más 2 más nuevos con al menos 5 años son:")
        print_sequence(wines.sort_by_age(self.data, min_age=5, descendant=True, limit=2))

    def test_group_by_ratings(self):
        print_test_header("group_by_ratings")

        print("\nPara puntuaciones con decimales:")
        grouped = wines.group_by_ratings(self.data)
        self._print_rated(grouped, 4.6)
        self._print_rated(grouped, 4.8)

        print("\n\nPara puntuaciones del 0-5 sin decimales:")
        grouped = wines.group_by_ratings(self.data, just_ints=True)
        self._print_rated(grouped, 2)

    @staticmethod
    def _print_rated(grouped: Dict[float, List[Wine]], rate: float):
        print("\nLos vinos con una puntuación de", rate, "son:")
        print_iterable(grouped[rate])


class CSVWinesTest(WinesTest):
    def __init__(self, dataset_path: str):
        super(CSVWinesTest, self).__init__(wines.parse_csv_file(dataset_path))


def main():
    test = CSVWinesTest("../data/wine_data.csv")

    # -- Entrega 1 --
    test.test_parse_file()

    # -- Entrega 2 --
    #  Bloque I
    test.test_filter_by_country()
    test.test_calculate_mean_age()

    #  Bloque II
    test.test_get_oldest_wines()
    test.test_sort_by_age()
    test.test_group_by_ratings()


if __name__ == "__main__":
    main()
