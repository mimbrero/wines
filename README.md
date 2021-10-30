# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso 2021/2022)
Autor/a: Alberto Mimbrero   uvus: albsanmim

Este proyecto trata y manipula información sobre vinos, como la adjuntada en la carpeta del proyecto <code>data/</code>, <code>wine_data.csv</code>.


## Estructura de las carpetas del proyecto

* **src/me/inetaddress/wines/**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **wines.py**: Módulo principal donde están las funciones para tratar los datos de vinos.
  * **wines_test.py**: Test de cada una de las funciones del módulo wines, explicado arriba.

  * **util/**: Paquete con módulos útiles:
    * **parsing_utils.py**: Módulo con funciones para parsear tipos que no se incluyen en builtins.

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

* **Wine**: tipo básico de un vino. Contiene toda la información explicada arriba (name, country, region, winery, rating, number_of_ratings, price, since, origin_appellation)

## Funciones implementadas
### wines.py

* **parse_file(str)**: Abre el archivo que se sitúa en la ruta dada como parámetro y lo parsea en una lista de tuplas de tipo Wine.

### wines_test.py

* **test_parse_file(str)**: Test para la función <code>parse_file(str)</code> del módulo <code>wines.py</code>. Requiere como parámetro la ruta de un archivo csv para hacer el test sobre él. Escribe en la consola el número de datos leídos, 3 objetos Wine que corresponden a los 3 primeros del archivo, y los 3 últimos.

### parsing_utils.py

* **parse_date(str)**: Parsea una date dada en str en formato <code>%d/%m/%Y</code> (dd/mm/aaaa).
