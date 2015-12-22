Implementación
====

Visualización de datos para la asignatura de **Diseño y Evaluación de Sistemas Interactivos**.
Los datos utilizados provienen de la iniciativa de datos abiertos como se dice en el informe de la práctica.
Estos datos provienen de la propuesta _Open data_ de las entidades públicas, que proviene de los gobiernos europeos con el fin de
promover el conocimiento y el uso de estos por la sociedad.

Primer boceto
----
En el informe que se entregó respecto a esta práctica, se dió unos bocetos que dividían la visualización en tres vistas distintas.
Debido a los factores que se describían en dicho informe se entregarán dos de las tres visualizaciones, que muestran los datos de:

- Distribución de producción de energía según tipo de energía
- Histórico de producción por cada tipo concreto de energía

Estructuras de las carpetas
----
```
.
├── css
│   └── style.css
├── data
│   ├── ciudades
│   └── energia
│       ├── energia_con_carbon.csv
│       ├── energia_eolica.csv
│       ├── energia_hidraulica.csv
│       ├── energia_nuclear.csv
│       ├── energia_primaria.csv
│       ├── energia_solar.csv
│       └── historicos
├── energia.html
├── favicon.ico
├── index.html
├── nvd3
├── README.md
└── script
    ├── csvunicode.py
    ├── csvunicode.pyc
    ├── generate-json.py
    ├── README.md
    ├── separate_categories.py
    └── separate_cities.py


```
`css`: contiene los estilos de las páginas de la visualización.

`data`: directorio que contiene los `csv` del dataset.
- _ciudades_: contiene los ficheros de datos respectivos a las ciudades. (_Los datos de las ciudades no se utilizan en esta implementación pero se tenían en una primera idea_)
- _energia_: contiene los ficheros de datos respectivos a los tipos de energía.
	- históricos: contienen los históricos por tipo de energía, al igual ocurre en el directorio `data/ciudades/`

`energía.html`: página dedicada a la visualización de datos según el tipo de energía que se escoga, está enlazada desde cada uno de los diagramas presentes en `index.html`. Al acceder se pasan por parámetros del método GET del navegador:
- `energia`: identificador del tipo de energía
- `title`: título/nombre del tipo de energía

`favicon.ico`: icono de la Escuela de Ingeniería Informática pixelizado como icono.

`index.html`: página principal de la visualización. Contiene los diagramas principales sobre la distribución de producción de energía por tipo de energía.

`nvd3`: directorio de la biblioteca externa para la visualización de areas apiladas. fuente: [http://nvd3.org](http://nvd3.org/examples/stackedArea.html)

`script`: el directorio contiene los scripts escritos en Python que se utilizaron para la modificación de los datos.

Por hacer
----

La siguiente lista describe las tareas que se propusieron en el primer boceto definido en el informe:

- [ ] Vista de visualización de los datos según las ciudades
- [ ] En la vista de `energia.html`, mostrar la relevancia del tipo de energía en la producción general de energía.

Referencias externas
----
**D3.js** biblioteca de Javascript para la visualización de diagramas en páginas web. Fuente: [http://d3js.org/](http://d3js.org/)

**NVD3** biblioteca de Javascript basada en D3.js, con abstracción de diferentes diagramas. Fuente: [http://nvd3.org/index.html](http://nvd3.org/index.html)

**Python doc - csv** módulo de Python para la lectura y escritura de archivos csv. Fuente: [PyDoc - csv](https://docs.python.org/2/library/csv.html)

**Python doc - json** módulo de Python para el reconocimiento de datos en JSON. Fuente: [PyDoc - json](https://docs.python.org/2/library/json.html)

Autor
----

Autor: Ismael José Taboada ([ismtabo](https://github.com/ismtabo))

Licencia: [GPL3](https://es.wikipedia.org/wiki/GNU_General_Public_License)
