# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso 2021/2022)
Autor/a: Alberto Mimbrero   uvus: albsanmim

Este proyecto trata y manipula información sobre vinos, como la adjuntada en la carpeta del proyecto <code>data/</code>, <code>wine_data.csv</code>.


## Estructura de las carpetas del proyecto

* **src/me/inetaddress/wines/**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **wines.py**: Módulo principal donde están las funciones para tratar los datos de vinos.
  * **wines_test.py**: Test de cada una de las funciones del módulo wines, explicado arriba.

  * **util/**: Paquete con módulos útiles:
    * **parsing_utils.py**: Módulo con funciones para parsear tipos que no se incluyen en builtins.
    * **test_utils.py**: Módulo con funciones útiles (su uso es muy repetido) para los tests.

* **data/**: Contiene el dataset o datasets del proyecto
    * **wine_data.csv**: Datos de 999 vinos distintos, desde su nombre, país o bodega hasta su precio, fecha o si tiene denominación de origen.

## Estructura del *dataset*

El dataset está compuesto por 9 columnas, con la siguiente descripción:

* **name**: de tipo <code>str</code>, representa el nombre del vino.
* **country**: de tipo <code>str</code>, representa el país de origen del vino.
* **region**: de tipo <code>str</code>, representa la región del país del vino.
* **winery**: de tipo <code>str</code>, representa la bodega de donde procede el vino.
* **rating**: de tipo <code>float</code>, representa la valoración media que los usuarios han dado al vino.
* **number_of_ratings**: de tipo <code>int</code>, representa el total de valoraciones dadas.
* **price**: de tipo <code>float</code>, representa el precio de una botella.
* **since**: de tipo <code>date</code>, representa desde cuándo existe el vino.
* **origin_appellation**: de tipo <code>bool</code>, representa si ha obtenido el certificado de denominación de origen.
....

## Tipos implementados

* **Wine**: tipo básico de un vino. Es una namedtuple. Contiene toda la información explicada arriba (name: str, country: str, region: str, winery: str, rating: float, number_of_ratings: int, price: float, since: date, origin_appellation: bool)

## Funciones implementadas
### wines.py

* **Entrega 1**

  * **parse_file(path: str)**: Abre el archivo que se sitúa en la ruta dada como parámetro y lo parsea en una lista de tuplas de tipo Wine.

* **Entrega 2**

  * Bloque I

    * **filter_by_country(wines: Iterable[Wine], country: str)**: Dado un Iterable que contiene una serie de <code>Wine</code>s, devuelve una lista de los vinos de ese iterable cuyo país de procedencia sea el país pasado como argumento.

    * ***calculate_age(wine: Wine, from_date: date = today)***: Función de ayuda. Dado un <code>Wine</code>, retorna su edad en años con decimales (estos decimales proceden del día y mes en el año de la fecha del vino). Si se proporciona una fecha en el parámetro from_date, la edad del vino será calculada a partir de esa fecha. En caso contrario, la fecha será la del momento de ejecución del código (HOY/today).
Primero calcula el timedelta entre el parámetro from_date y la fecha del vino. Luego convierte a días ese timedelta, y lo divide entre 365. La salida está redondeada a 2 decimales.

    * **calculate_mean_age(wines: Iterable[Wine], from_date: date = today)**: Dado un Iterable que contiene una serie de <code>Wine</code>s, devuelve la media de edad de todos esos vinos. La edad se calcula con la función <code>calculate_age</code>. Al igual que en esa función, si se pasa como parámetro from_date una fecha, la edad de los vinos será calculada con esa fecha. Si no es proporcionada, será la del momento de ejecución del código (HOY/today). 
Primero crea un Iterable con la edad de cada vino y posteriormente hace la media de ese Iterable.

  * Bloque II

    * **get_oldest_wines(wines: Iterable[Wine])**: Dado un Iterable que contiene una serie de <code>Wine</code>s, retorna una lista con los <code>Wine</code>s que tengan la fecha más antigua del Iterable wines. 
Primero calcula la fecha más antigua entre todos los vinos del Iterable pasado como argumento. Posteriormente, retorna una lista con los vinos que tengan esa fecha. Probablemente sea solo uno.

    * **sort_by_age(wines: Iterable[Wine], descendant: bool = False, min_age: float = 0, limit: int = -1, from_date: date = today)**: Dado un Iterable que contiene una serie de <code>Wine</code>s,  retorna una lista que contiene los vinos del Iterable wines con edad superior o igual a la especificada en el parámetro min_age, ordenada por fecha de los vinos, de manera ascendente o descendente, especificado por el parámetro descendant. 
Se puede especificar el parámetro limit, que trunca la lista al número de resultados especificado por ese parámetro (si es menor que 1, no se truncará). 
Si se proporciona una fecha en el parámetro from_date, la edad de los vinos para el filtrado de min_age será calculada a partir de esa fecha. En caso contrario, la fecha será la del momento de ejecución del código (HOY/today). 
Primero crea una lista a partir del Iterable pasado como argumento solo con los vinos cuya edad sea mayor al parámetro min_age. Posteriormente, ordena la lista por fecha en orden descendente, y la retorna.

    * **group_by_ratings(wines: Iterable[Wine], just_ints: bool = False)**: Dado un Iterable que contiene una serie de <code>Wine</code>s, devuelve un diccionario en el que las claves representan una valoración (y si el parámetro just_ints es True, las claves solo serán números enteros), y el valor es una lista con los vinos que tienen esa valoración (o si el parámetro just_ints es True, la lista contendrá los vinos cuya valoración sin decimales sea esa valoración).
Primero crea un defaultdict cuya factory es la función list. Luego, añade cada vino del Iterable pasado como argumento a la lista del diccionario cuya clave es la valoración del vino. La clave será su valoración exacta si el parámetro just_ints es False, o su valoración truncada si just_ints es True.

### wines_test.py

En el módulo de pruebas se han definido las siguientes funciones de pruebas, cada una de las cuales se usa para probar la función que tiene el mismo nombre (pero sin comenzar por <code>test_</code> del módulo <code>wines</code>. Por ejemplo, la función <code>test_parse_file</code> prueba la función <code>parse_file</code>.

* **test_parse_file(path: str)**
* **test_filter_by_country(data: Sequence[Wine])**
* **test_calculate_mean_age(data: Sequence[Wine])**
* **test_get_oldest_wines(data: Sequence[Wine])**
* **test_sort_by_age(data: Sequence[Wine])**
* **test_group_by_ratings(data: Sequence[Wine])**

En el módulo también se han definido 2 funciones auxiliares:
* **filter_by_country_and_print(data: Sequence[Wine], country: str)**
* **print_rated(grouped: Dict[float, List[Wine]], rate: float)**

### parsing_utils.py

* **parse_date(to_parse: str)**: Parsea una date dada en str en formato <code>%d/%m/%Y</code> (dd/mm/aaaa).

### test_utils.py

* **print_test_header(test_name: str)**: Imprime un mensaje que informa sobre el test que se va a ejecutar (pasado por el parámetro test_name) que también sirve de separador.

* **print_iterable(iterable: Iterable[object], before: str = " ", after: str = "")**: Imprime un iterable de forma muy visible o, si está vacío, "The given iterator is empty!". Se puede personalizar la identación de la impresión con el parámetro before, y los caracteres posteriores con el parámetro after.

* **print_sequence(sequence: Sequence[object], before: str = " ", after: str = "")**: Imprime una secuencia (lista, tupla...) en orden de forma muy visible (incluyendo la posición de cada elemento) o, si está vacía, "The given sequence is empty!". Se puede personalizar la identación de la impresión con el parámetro before, y los caracteres posteriores con el parámetro after.