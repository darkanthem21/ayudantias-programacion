def estudiantesPorNivel(estudiantes: dict, nivel: str) -> list:
    pass

def progresoEstudiante(inscripciones: list, cursos: dict, ID: str) -> dict:
    pass

def analizarCurso(codigo_curso: str, inscripciones: list) -> dict:
    pass

def main():
    # Datos de ejemplo
    estudiantes = {
        '12345': ('María', 'maria@example.com', 'Avanzado'),
        '67890': ('Juan', 'juan@example.com', 'Intermedio'),
        '54321': ('Pedro', 'pedro@example.com', 'Intermedio'),
        '98765': ('Ana', 'ana@example.com', 'Avanzado')
    }

    cursos = {
        'BIO101': ('Biología Celular', 5, 'Introductorio', []),
        'BIO201': ('Genética', 6, 'Avanzado', ['BIO101']),
        'MAT101': ('Álgebra Lineal', 4, 'Introductorio', []),
        'MAT201': ('Cálculo Diferencial', 5, 'Intermedio', ['MAT101']),
        'MAT301': ('Cálculo Integral', 5, 'Intermedio', ['MAT201']),
        'BIO301': ('Biología Molecular', 6, 'Avanzado', ['BIO201'])
    }

    inscripciones = [
        ('12345', 'BIO101', 2023, 1, 3.5, 'Aprobado'),
        ('12345', 'BIO201', 2023, 2, 4.0, 'Aprobado'),
        ('67890', 'BIO101', 2023, 1, 2.8, 'Aprobado'),
        ('54321', 'MAT101', 2023, 1, 3.0, 'Aprobado'),
        ('98765', 'BIO101', 2023, 1, 2.5, 'Reprobado'),
        ('98765', 'BIO201', 2023, 2, 3.8, 'Aprobado'),
        ('98765', 'MAT101', 2023, 1, 4.0, 'Aprobado'),
        ('12345', 'MAT101', 2023, 1, 3.7, 'Aprobado'),
        ('12345', 'MAT201', 2023, 2, 4.2, 'Aprobado'),
        ('67890', 'BIO201', 2023, 2, 3.1, 'Aprobado'),
        ('67890', 'MAT101', 2023, 1, 2.9, 'Reprobado'),
        ('54321', 'BIO101', 2023, 1, 3.8, 'Aprobado'),
        ('98765', 'MAT201', 2023, 2, 3.2, 'Reprobado'),
        ('98765', 'BIO301', 2023, 2, 4.1, 'Aprobado'),
    ]

    # Ejemplo de uso
    print("Estudiantes en el nivel Avanzado:", estudiantesPorNivel(estudiantes, 'Intermedio'))
    print("Progreso del estudiante con ID '12345':", progresoEstudiante(inscripciones, cursos, '12345'))
    print("Análisis del curso 'MAT201':", analizarCurso('MAT201', inscripciones))

if __name__ == "__main__":
    main()
