# Exploradores de la Federacion
La Federación Galáctica ha enviado un equipo de exploradores para investigar diversos planetas en la galaxia. Cada explorador ha registrado sus exploraciones en una lista de tuplas, donde cada tupla contiene los siguientes elementos:

-  **ID del Explorador**  (String)
-  **Código del Planeta** (*String*)
-  **Monto de Exploración** (*Int*)
-  **Desafíos Completados** (*Int*)

Se nos entrega un diccionario anidado con los datos de cada explorador

`exploradores = {
"E001": {"nombre": "Han Solo", "expediciones": 0, "desafios_completados": 0},
"E002": {"nombre": "Chewbacca", "expediciones": 0, "desafios_completados": 0},
"E003": {"nombre": "Leia Organa", "expediciones": 0, "desafios_completados": 0},
"E004": {"nombre": "Luke Skywalker", "expediciones": 0, "desafios_completados": 0}
}`

y una lista de tuplas que contiene las exploraciones realizadas

`exploraciones = [("E004", "Tatooine", 1400, 2),("E003", "Coruscant", 1100, 1),
("E002", "Naboo", 400, 1),("E001", "Endor", 900, 1)]`

Vamos a realizar un programa que cumpla con las siguientes funciones:

### a) Actualizar los datos de los exploradores

Para esto usaremos la funcion **`resumen_exploraciones(exploraciones: list, exploradores: dict) -> None`**: Esta función recibe como entrada una lista de exploraciones y un diccionario que contiene información sobre los exploradores. Actualiza el diccionario de exploradores con la cantidad de expediciones realizadas, la cantidad total de desafíos completados y el monto total de créditos obtenidos por cada explorador.

### b) Crear un diccionario con las exploraciones de cada planeta
Crearemos la funcion **`exploraciones_por_planeta(exploraciones: list) -> dict`**: Esta función recibe como entrada una lista de exploraciones y genera un resumen de las exploraciones agrupadas por planeta. Devuelve un diccionario donde cada clave es el nombre del planeta y cada valor es otro diccionario con el monto total de créditos obtenidos y la cantidad total de desafíos completados en ese planeta.
Cada elemento del nuevo diccionario debe tener la forma:
`"NombrePlabeta" : {"monto_total": monto, "desafios completados" : total desafios}`

### c) Mostrar los datos de salida de forma estetica usando formateo de strings

Ejemplo:

![Salida](https://ibb.co/LhDG6bf)

