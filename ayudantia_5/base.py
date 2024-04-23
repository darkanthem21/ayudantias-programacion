## Retorna una lista con las entretenciones cuya puntuacion sea mayor o igual a puntuacion
def filtrar(entretencion: list, puntuacion:int) -> list:
    pass

## Retorna el promedio de dias que acuden las personas a la entretencion e.
def promedio_dias(turistas: dict, entretencion: list, e: str) -> float:
    pass


## turistas_por_entretencionr debe retornar un diccionario que asocie el nombre de la entretencion a 
## una lista de codigos de turistas que han visitado esa entretencion. La lista debe estar ordenada ascendentemente
def turistas_por_entretencion(turistas: dict, entretencion: list) -> dict:
    pass

def main():
    turistas = {132: ('Mario Vasquez', 6, 3),
                13 : ('Maria Ines Campos', 11, 4),
                58 : ('Vicente Cush', 5, 4),
                342 : ('Mario Neta', 7, 2),
                789: ('Eliza Noriega', 7, 5),
                76: ('Amalia Alvarez', 2, 3),
                87: ('Adolfo Rivera',7,1)
                }
    
    entretencion = [('Buceo',5), ('Masajes',6), ('Casino',4), ('Piscina',7),
                    ('Playa',4),('Surf',7), ('Baile entretenido',2), ('Teatro',5),
                    ('Restaurant',6), ('Karaoke',4), ('Bingo',7), ('Cine',5),
                    ('Bar',1), ('Spa',5), ('Gimnasio',4),('Cabalgata',2)]
    
    # Funcion 1
    print(filtrar(entretencion, 5))
    
    # Funcion 2 
    print("Promedio:", promedio_dias(turistas, entretencion), 'Bingo')
    print("Promedio:", promedio_dias(turistas, entretencion), 'Bar')

    # Funcion 3
    entretencionPersonas = turistas_por_entretencion(turistas, entretencion)

    # Si terminaste las funciones rapido y
if __name__ == "__main__":
    main()
