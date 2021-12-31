from typing import Callable, Dict, Tuple

import matplotlib.pyplot as plt


def generate_pie_chart(title: str,
                       data: Dict[str, int],
                       inner_label: Callable[[float], str] = None,
                       others_percentage: float = 0.03,
                       others_label: str = "Others") -> None:

    data = _group_others(data, others_percentage, others_label)
    labels, values = _sort_and_unzip_labels_and_values(data, others_label)

    plt.title(title)
    plt.pie(values, labels=labels, shadow=True, autopct=inner_label)

    plt.show()


def _group_others(data: Dict[str, int], percentage, others_label: str) -> Dict[str, int]:
    data = dict(data)  # Don't mutate the given dictionary
    total = sum(data.values())
    max_allowed = total * percentage

    for label, value in tuple(data.items()):  # Concurrency. Store #items() before iterating because the dict changes
        if value <= max_allowed:
            del data[label]
            data[others_label] = data.get(others_label, 0) + value

    return data


def _sort_and_unzip_labels_and_values(data: Dict[str, int], others_label) -> Tuple[str, int]:
    items = sorted(data.items(), key=lambda item: item[1], reverse=True)
    labels, values = [list(generator_item) for generator_item in zip(*items)]  # Unzip, reverse zip operation [1]

    # Make "others" be at the end
    if others_label in data:
        index = labels.index(others_label)
        labels.append(labels.pop(index))
        values.append(values.pop(index))

    return labels, values

# [1] (https://stackoverflow.com/questions/12974474/how-to-unzip-a-list-of-tuples-into-individual-lists)
