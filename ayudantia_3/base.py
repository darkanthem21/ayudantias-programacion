def calcular_ganancias_por_empleado(registro_ventas_diarias: dict, inventario: dict) -> dict:
    ganancias_por_empleado = {}
    for ventas in registro_ventas_diarias.values():
        for venta in ventas:
            empleado = venta["empleado"]
            titulo_libro = venta["titulo"]
            if titulo_libro in inventario:
                precio_venta = inventario[titulo_libro]["precio"]
                costo_libro = inventario[titulo_libro]["costo"]
                ganancia = precio_venta - costo_libro
                if empleado not in ganancias_por_empleado:
                    ganancias_por_empleado[empleado] = 0
                ganancias_por_empleado[empleado] += ganancia
    return ganancias_por_empleado

def calcular_ganancias_por_genero_y_empleado(registro_ventas_diarias: dict, genero_deseado: str, empleado_deseado: str, inventario: dict) -> float:
    ganancias_por_genero_y_empleado = 0
    for ventas in registro_ventas_diarias.values():
        for venta in ventas:
            empleado = venta["empleado"]
            titulo_libro = venta["titulo"]
            if titulo_libro in inventario and genero_deseado in inventario[titulo_libro]["generos"] and empleado == empleado_deseado:
                precio_venta = inventario[titulo_libro]["precio"]
                costo_libro = inventario[titulo_libro]["costo"]
                ganancia = precio_venta - costo_libro
                ganancias_por_genero_y_empleado += ganancia
    return ganancias_por_genero_y_empleado

def main():
        # Diccionario de inventario con más libros
    inventario = {
        "El Hobbit": {"costo": 10000, "cantidad": 20, "precio": 20000, "generos": ["Fantasía", "Aventura"]},
        "1984": {"costo": 8000, "cantidad": 30, "precio": 18000, "generos": ["Ciencia Ficción", "Distopía"]},
        "Cien años de soledad": {"costo": 12000, "cantidad": 25, "precio": 25000, "generos": ["Realismo Mágico", "Literatura Latinoamericana"]},
        "Don Quijote": {"costo": 15000, "cantidad": 15, "precio": 30000, "generos": ["Novela Clásica", "Sátira"]},
        "Harry Potter y la piedra filosofal": {"costo": 11000, "cantidad": 35, "precio": 22000, "generos": ["Fantasía", "Magia"]},
        "Los juegos del hambre": {"costo": 9000, "cantidad": 40, "precio": 20000, "generos": ["Ciencia Ficción", "Aventura"]},
        "El nombre del viento": {"costo": 13000, "cantidad": 20, "precio": 24000, "generos": ["Fantasía", "Aventura"]},
        "Orgullo y prejuicio": {"costo": 14000, "cantidad": 15, "precio": 28000, "generos": ["Novela Romántica", "Clásicos"]}
    }

    # Registro de ventas con más ventas diarias
    registro_ventas_diarias = {
        "2024-04-01": [
            {"titulo": "El Hobbit", "empleado": "Juan"},
            {"titulo": "1984", "empleado": "Ana"},
            {"titulo": "Cien años de soledad", "empleado": "Juan"}
        ],
        "2024-04-02": [
            {"titulo": "1984", "empleado": "Ana"},
            {"titulo": "Cien años de soledad", "empleado": "Juan"},
            {"titulo": "Don Quijote", "empleado": "Pedro"}
        ],
        "2024-04-03": [
            {"titulo": "El Hobbit", "empleado": "Juan"},
            {"titulo": "Don Quijote", "empleado": "Pedro"},
            {"titulo": "Cien años de soledad", "empleado": "Ana"}
        ],
        "2024-04-04": [
            {"titulo": "Harry Potter y la piedra filosofal", "empleado": "Juan"},
            {"titulo": "Los juegos del hambre", "empleado": "Ana"},
            {"titulo": "El nombre del viento", "empleado": "Pedro"}
        ],
        "2024-04-05": [
            {"titulo": "El Hobbit", "empleado": "Juan"},
            {"titulo": "Harry Potter y la piedra filosofal", "empleado": "Ana"},
            {"titulo": "Orgullo y prejuicio", "empleado": "Pedro"}
        ]
    }

    # Ejemplo de uso
    ganancias_por_empleado = calcular_ganancias_por_empleado(registro_ventas_diarias, inventario)
    print("Ganancias por empleado:")
    for empleado, ganancia in ganancias_por_empleado.items():
        print(f"{empleado}: ${ganancia}")

    genero_deseado = "Fantasía"
    empleado_deseado = "Juan"
    ganancias_por_genero_y_empleado = calcular_ganancias_por_genero_y_empleado(registro_ventas_diarias, genero_deseado, empleado_deseado, inventario)
    print(f"\nGanancias por ventas de libros de género '{genero_deseado}' realizadas por '{empleado_deseado}': ${ganancias_por_genero_y_empleado}")


if __name__ == '__main__':
    main()