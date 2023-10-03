# CRUD
Crud Auber

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
## _Introduccion a CRUD_
La funcionalidad CRUD, que significa Crear, Leer, Actualizar y Eliminar, es una parte fundamental de muchas aplicaciones web. Permite interactuar con una base de datos de manera efectiva al crear, leer, actualizar y eliminar registros. En este repositorio, implementamos esta funcionalidad utilizando el framework Django,base de datos Sqlite3.

## Diseno Ingenieria

![](https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2021/06/Control-Flow-Of-MVT.jpg)

Django utiliza el patrón de diseño Modelo-Vista-Controlador (MVC), que en Django se conoce como Modelo-Plantilla-Vista (MVT). A continuación, se describe cómo funciona este patrón en Django:

- **Modelo:** Representa la estructura de la base de datos y define cómo se almacenan los datos. En Django, los modelos se definen como clases Python y se utilizan para crear tablas en la base de datos.En términos sencillos, el modelo en Django se refiere a cómo organizamos y almacenamos nuestros datos en la base de datos. Puedes pensar en ello como una representación de nuestras tablas de base de datos utilizando clases Python.

- **Plantilla:**  La plantilla es la parte de nuestra aplicación que se encarga de cómo se ve y se presenta la información al usuario. Se utiliza HTML para diseñar la apariencia de nuestras páginas web, y además, podemos usar las etiquetas de plantilla de Django para mostrar dinámicamente datos desde el controlador (vista).


- **Vista:** En el contexto del patrón MVT de Django, la vista sería similar al "cerebro" de nuestra aplicación. Aquí es donde manejamos la lógica de cómo nuestra aplicación responde a las solicitudes del usuario. En otras palabras, las vistas son como las funciones o clases que se ocupan de interactuar con los modelos y las plantillas para crear una respuesta web que se envía de vuelta al usuario.
