Scripts para modificación de los datos
====

La carpeta `script` contiene los programas utilizados para extrarer los datos de la fuente original. Los dos scripts utilizados son :
- `separate_categories`
- `generate-json`

Estos scripts están escritos en Python y basados fundamentalmente en el módulo `csv` para la lectura de los ficheros del dataset.

`separate_categories`
----

Script en Python para separar las categorías de datos en el csv de la Junta de Castilla y León, dataset para la práctica final de la asignatura Diseño y Evaluación de Sistemas Interactivos.

Este programa separará los datos mediante los valores de la primera columna. Haciendo uso de la primera frase contenida en ella (caracter de la separación '`.`'). Y genera distintos ficheros `csv` con cada uno de los _sub-dataset_.

Ha sido utilizado para hacer al disgregación de los datos según su categoría, tomando como fuente el fichero en bruto obtenido de la página de la Junta de Castilla y León de Open data.

`separate_cities`
----
Este programa separará los datos mediante los valores de la primera columna, las ciudades, una vez han sido separadas las categorias. Cambia la primera columna, extrayendo el nombre de la ciudad y cambiándolo por el tipo de energía. Y genera distintos ficheros `csv` con cada una de las ciudades.

`generate-json`
----
Script en Python para convertir una tabla csv con la estructura generada por el anterior programa a **JSON** para hacer más sencilla la lectura de los datos mediante Javascript.

Este script toma la primera columna para agrupar los datos -tipo de energía, ciudad-, y las columnas 2 y 3 (años y valor) para generar un array de pares de coordenadas (columna 2, columna 3).

Uso
----

```bash
$ python <script> path-csv-file destination-path
```
`script`: fichero de python según el programa que queramos utilizar.

`path-csv-file`: ruta hasta fichero csv.

`destination-path`: ruta destino para guardar los ficheros csv generados.

Sobre el autor
----

Autor: Ismael José Taboada ([ismtabo](https://github.com/ismtabo))

Licencia: [GPL3](https://es.wikipedia.org/wiki/GNU_General_Public_License)
