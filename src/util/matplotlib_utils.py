from typing import Callable, Dict, Tuple

import matplotlib.pyplot as plt


def generate_pie_chart(title: str,
                       data: Dict[str, int],
                       inner_label: Callable[[float], str] = None,
                       others_percentage: float = 0.03,
                       others_label: str = "Others") -> None:
    """
    Genera un gráfico circular o de pastel con un título, etiquetas interiores y exteriores, agrupando los valores
    con porcentaje sobre el total menor o igual a others_percentage y etiqueta others_label sobre los datos pasados
    como parámetro.

    @param title: título del gráfico
    @param data: diccionario cuyas claves son las etiquetas de cada trozo del pastel y los valores son el valor
     numérico que corresponde a esa etiqueta
    @param inner_label: Callable que tiene como parámetro el porcentaje de un trozo del pastel y retorna una string para
     ser puesta sobre el trozo del pastel. None si no se quiere usar, por defecto None
    @param others_percentage: porcentaje máximo sobre el total que debe tener un valor para ser agrupado con otros de
     ese o menor porcentaje en un solo trozo del pastel. Por defecto 0.03 (3 %)
    @param others_label: etiqueta que tendrá la agrupación de datos con porcentaje menor o igual a others_percentage.
     Por defecto "Others"
    """

    data = _group_others(data, others_percentage, others_label)
    labels, values = _sort_and_unzip_labels_and_values(data, others_label)

    plt.title(title)
    plt.pie(values, labels=labels, shadow=True, autopct=inner_label)

    plt.show()


def _group_others(data: Dict[str, int], percentage, others_label: str) -> Dict[str, int]:
    """
    Dado un diccionario cuyas claves son las etiquetas de cada trozo del pastel y los valores son el valor numérico
    que corresponde a esa etiqueta, devuelve ese diccionario agrupando en la etiqueta others_label las que tengan
    como valor un porcentaje menor o igual al pasado como parámetro percentage sobre el total.

    @param data: datos a aplicar la función
    @param percentage: porcentaje máximo que debe tener un dato para agruparlo
    @param others_label: etiqueta que tendrá la agrupación
    @return:
    """
    data = dict(data)  # Don't mutate the given dictionary
    total = sum(data.values())
    max_allowed = total * percentage

    for label, value in tuple(data.items()):  # Concurrency. Store #items() before iterating because the dict changes
        if value <= max_allowed:
            del data[label]
            data[others_label] = data.get(others_label, 0) + value

    return data


def _sort_and_unzip_labels_and_values(data: Dict[str, int], others_label) -> Tuple[str, int]:
    """
    Ordena los datos de mayor a menor, dejando la etiqueta others_label al final. Devuelve esos datos separados en
     una lista con las etiquetas y otra lista con los valores.

    @param data: datos a ordenar y devolver
    @param others_label: etiqueta que quedará al final, la agrupación de los datos menores a un porcentaje.
    @return: una tupla con dos listas, la primera con las etiquetas y la segunda con los valores, en orden.
    """
    items = sorted(data.items(), key=lambda item: item[1], reverse=True)
    labels, values = [list(generator_item) for generator_item in zip(*items)]  # Unzip, reverse zip operation [1]

    # Make "others" be at the end
    if others_label in data:
        index = labels.index(others_label)
        labels.append(labels.pop(index))
        values.append(values.pop(index))

    return labels, values

# [1] (https://stackoverflow.com/questions/12974474/how-to-unzip-a-list-of-tuples-into-individual-lists)
