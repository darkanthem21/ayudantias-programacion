# Seguimiento Académico en una Universidad

La Escuela de Biología mantiene un sistema que registra información sobre sus estudiantes, los cursos ofrecidos en la carrera y las inscripciones de los estudiantes en los cursos mediante diccionarios y listas. Aquí está la estructura de datos:
```python 
## Inscripciones guarda todas las inscripciones de los estudiantes
inscripciones = [
    ('12345', 'BIO101', 2023, 1, 3.5, 'Aprobado'),
    ('12345', 'BIO201', 2023, 2, 4.0, 'Aprobado')
]
    # (id alumno, curso, anno tomado, nota, situacion final)
```

```python 
## Todos los estudiantes y su respectivo ciclo academico
    estudiantes = {
        '12345': ('María', 'maria@example.com', 'Avanzado'),
        '67890': ('Juan', 'juan@example.com', 'Intermedio'),
        '54321': ('Pedro', 'pedro@example.com', 'Intermedio'),
        '98765': ('Ana', 'ana@example.com', 'Avanzado')
    }
    # 'id alumno': (Nombre, Correo, Ciclo academico)
```

```python 
## Todos los estudiantes y su respectivo ciclo academico
    cursos = {
        'BIO101': ('Biología Celular', 5, 'Introductorio', []),
        'BIO201': ('Genética', 6, 'Avanzado', ['BIO101']),
        'MAT101': ('Álgebra Lineal', 4, 'Introductorio', []),
        'MAT201': ('Cálculo Diferencial', 5, 'Intermedio', ['MAT101']),
        'MAT301': ('Cálculo Integral', 5, 'Intermedio', ['MAT201']),
        'BIO301': ('Biología Molecular', 6, 'Avanzado', ['BIO201'])
    }
    # 'id Curso': (Nombre, Creditos, Ciclo academico, [prerrequisitos], )
```

## Funciones a implementar

1. **Listar Estudiantes por Nivel**
   - La función `estudiantesPorNivel(estudiantes: dict, nivel: str) -> list` recibe un diccionario con información de estudiantes y un nivel académico, y devuelve una lista con los datos de los estudiantes que pertenecen a ese nivel.

   **Ejemplo de Uso:**
   ```python
   nivel = 'Intermedio'

   # Resultado esperado
   # [('67890', 'Juan', 'juan@example.com'), ('54321', 'Pedro', 'pedro@example.com')]
   print(estudiantesPorNivel(estudiantes, nivel))
2. **Progreso de cada estudiante** 

    La función `progresoEstudiante(inscripciones: list, cursos: dict, ID: str) -> dict` calcula el progreso académico de un estudiante en función de sus inscripciones a cursos y la información de los cursos.

    **Ejemplo de Uso:**
    ```python
    ID_estudiante = '12345'
    # Resultado esperado
    # {'Introductorio': 9, 'Avanzado': 6}
    print(progresoEstudiante(inscripciones, curso,ID_estudiante))
3. **Análisis de Cursos**

    La función `analizar_curso(codigo_curso: str, inscripciones: list) -> dict` proporciona estadísticas detalladas sobre un curso específico, incluyendo el promedio de notas, la distribución de notas, el porcentaje de aprobados y reprobados, y el total de estudiantes inscritos en el curso.

    **Ejemplo de Uso:**
    ```python
    codigo_curso = 'BIO101'

    # {'Promedio': 3.0, 'Distribución de Notas': {3.5: 1, 2.8: 1, 2.5: 1}, 'Porcentaje de Aprobados': 66.67, 'Porcentaje de Reprobados': 33.33, 'Total de Estudiantes': 3}
    print(analizar_curso(codigo_curso, inscripciones))
