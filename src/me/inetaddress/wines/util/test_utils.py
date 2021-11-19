from typing import Iterable


def print_test_header(test_name: str) -> None:
    print("\n\n--------------------------------------")
    print(test_name, "test")
    print("--------------------------------------")


def print_iterable(iterable: Iterable, before: str = " ", after: str = "") -> None:
    for i in iterable:
        print(f"{before}- {i}{after}")
