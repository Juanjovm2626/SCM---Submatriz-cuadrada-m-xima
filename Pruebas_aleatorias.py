import pytest
import random
from Solucion_Fuerzabruta import largestsquare_bruteforce
from Solucion_Tabulacion import Solucion_Tabulacion


algorithms = [
    ("brute force", largestsquare_bruteforce),
    #("divide & conquer", knapsack_divide_conquer),
    ("tabulation", Solucion_Tabulacion)
]

def generate_matrix_tests(n_tests=10):
    matrix_cases = []

    for i in range(n_tests):
        # 1. Definimos dimensiones de la matriz principal (Lienzo)
        rows = random.randint(5, 15)
        cols = random.randint(5, 15)
        
        # 2. Creamos la matriz con valores aleatorios (ej. 0 a 9)
        matrix = [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]

        # 3. Generamos una submatriz cuadrada aleatoria dentro de los límites
        # Determinamos el tamaño máximo posible para que sea cuadrada
        max_side = min(rows, cols)
        side = random.randint(2, max_side)
        
        # Elegimos una posición de origen (esquina superior izquierda) válida
        start_row = random.randint(0, rows - side)
        start_col = random.randint(0, cols - side)

        # 4. Extraemos la submatriz (esto sirve para validar tus algoritmos)
        submatrix = []
        for r in range(start_row, start_row + side):
            submatrix.append(matrix[r][start_col : start_col + side])

        # 5. Guardamos el caso
        # Formato: (Nombre, Matriz_Completa, Tamaño_Sub, Posicion_Esperada, Submatriz_Resultante)
        case_name = f"matrix_case_{i+1}"
        expected_pos = (start_row, start_col)
        
        matrix_cases.append({
            "name": case_name,
            "full_matrix": matrix,
            "sub_side": side,
            "origin": expected_pos,
            "submatrix": submatrix
        })

    return matrix_cases


@pytest.mark.parametrize("algorithm_name, algorithm", algorithms)
@pytest.mark.parametrize("name, full_matrix, sub_side, origin, submatrix", generate_matrix_tests())

def test_largestsquare(algorithm_name, full_matrix, sub_side, origin, submatrix):
    """
    Prueba cada algoritmo con cada caso de prueba.
    """
    # Ejecutamos el algoritmo (con 3 parámetros como acordamos)
    result = algorithm(full_matrix)

    # Verificamos el resultado numérico
    assert result == sub_side
