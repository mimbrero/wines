from typing import Iterable, Sequence


def print_test_header(test_name: str) -> None:
    print("\n\n--------------------------------------")
    print(test_name, "test")
    print("--------------------------------------")


def print_iterable(iterable: Iterable, before: str = " ", after: str = "") -> None:
    """
    Prints one by one the elements of the given iterable.
    """
    if not any(iterable):  # If it's empty
        print(f"{before}The given iterator is empty!")
        return

    for item in iterable:
        print(f"{before}- {item}{after}")


def print_sequence(sequence: Sequence, before: str = " ", after: str = "") -> None:
    """
    Prints one by one the elements of the given sequence (an ORDERED (tuple, list...) iterable).
    """
    if not sequence:  # If it's empty
        print(f"{before}The given sequence is empty!")
        return

    for i, item in enumerate(sequence):
        print(f"{before}[{i}] {item}{after}")
