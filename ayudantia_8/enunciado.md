
# Encontrar numeros palindromos en un archivo
El ejercicio se explica de una manera muy simple, se requiere crear cuatro funciones.

 - **es_palindromo(numero: str) -> bool** : esta funcion debe clasificar una cadena  y ver si es palindromo o no de manera recursiva (Numero cuyos digitos están dispuestos de tal manera que resulta la misma leída de izquierda a derecha que de derecha a izquierda
 - **leer_numeros(nombre_archivo: str) -> list** : funcion que recibe el nombre de un archivo como string, recorre todas sus lineas y devuelve una lista con todos los numeros a clasificar, usar manejo de excepciones para los casos particulares de los archivos
 - **procesar_numero(numero: str) -> str**: esta funcion toma UNA cadena de texto que representa una linea del archivo 'entradas.txt' y la clasifica. La funcion debe retornar un String dependiendo de cada uno de los siguientes casos. Usa manejo de excepciones en caso de un valor no valido.
	-  Si la cadena no existe, se la salta.
	- Identificar un numero negativo y no procesarlo.
	- Identificar si el numero es o no palindromo.
	- El objetivo es que para todos los elementos de entradas.txt se genere un
	string con el siguiente formato:
	```python
	"2145624: No es un palíndromo"
	"48828123: No es un palíndromo"
	"121: es un palíndromo"
	"hola: Valor no valido, se omite"
- **escribir_resultados(nombre_archivo: str, resultados: list) -> None**: Esta funcion escribe en el archivo salidas.txt todos los strings que generaste en la funcion anterior, usa manejo de excepciones en caso de que haya algun error al escribir el archivo
	
	



