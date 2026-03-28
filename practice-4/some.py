def determinant(matrix):
    """
    Вычисляет детерминант матрицы рекурсивно (разложение по первой строке)
    
    :param matrix (list of list of float): матрица для вычисления детерминанта
    :return (float): детерминант матрицы
    """
    # Базовый случай: матрица 1x1
    if len(matrix) == 1:
        return matrix[0][0]
    
    # Базовый случай: матрица 2x2
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Рекурсивный случай: матрица 3x3 и больше
    det = 0
    for j in range(len(matrix)):
        # Знак (-1)^(0+j)
        sign = 1 if j % 2 == 0 else -1
        
        # Минор: удаляем первую строку и j-й столбец
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        
        # Рекурсивный вызов
        det += sign * matrix[0][j] * determinant(minor)
    
    return det


# Пример использования
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

det = determinant(matrix)
print(f"Детерминант матрицы: {det}")