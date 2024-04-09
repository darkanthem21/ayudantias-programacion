## Ejercicio libreria

Una libreria desea llevar un registro de sus ventas diarias para analizar el desempeño de sus empleados y de los distintos géneros de libros que venden. Para ello, se te proporciona un registro de ventas diarias y un inventario de libros disponibles en la librería.

El registro de ventas diarias se presenta como un diccionario donde cada clave representa una fecha (en formato AAAA-MM-DD) y el valor asociado es una lista de diccionarios. Cada diccionario en la lista representa una venta y contiene el título del libro vendido y el nombre del empleado que realizó la venta.

El inventario de libros está representado por un diccionario donde las claves son los títulos de los libros y los valores son diccionarios que contienen información sobre el costo, la cantidad disponible, el precio de venta y los géneros a los que pertenece cada libro.

Necesitamos implementar dos funciones:

1.  `calcular_ganancias_por_empleado(registro_ventas_diarias: dict, inventario: dict) -> dict`: Esta función debe calcular las ganancias generadas por cada empleado, teniendo en cuenta los costos de los libros y el precio al que se venden. (Ganancia = precio - costo_libro)
    
2.  `calcular_ganancias_por_genero_y_empleado(registro_ventas_diarias: dict, genero_deseado: str, empleado_deseado: str, inventario: dict) -> float`: Esta función debe calcular las ganancias generadas por un empleado en particular a través de las ventas de libros de un género específico. Por ejemplo: Necesito saber cuantas ganancias genero Juan vendiendo libros del genero: Fantasia	
