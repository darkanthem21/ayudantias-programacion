def calcular_suma_numeros(archivo):
    suma_total = 0
    num_lineas = 0

    with open(archivo, 'r') as file:
        for linea in file:
            numero = int(linea.strip())
            suma_total += numero
            num_lineas += 1

    return suma_total, num_lineas

archivos_prueba = ["datos.txt", "datos_con_errores.txt", "archivo_inexistente.txt"]

for archivo in archivos_prueba:
    print(f"\nProcesando '{archivo}':")
    suma, num_lineas = calcular_suma_numeros(archivo)
    if num_lineas > 0:
        promedio = suma / num_lineas
        print(f"El promedio de los números en '{archivo}' es: {promedio}")
    else:
        print(f"No se pudo calcular el promedio para '{archivo}' porque no contiene números válidos.")
