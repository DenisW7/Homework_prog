def draw_symbol_plot(func, bottom_edge, top_edge, string_count):
    """
    Выводит график функции в консоль в виде символов

    :param func (function): функция для построения графика
    :param bottom_edge (float): нижняя граница диапазона x
    :param top_edge (float): верхняя граница диапазона x
    :param string_count (int): количество строк для вывода
    """
    # Вычисляем шаг по оси x
    x_step = (top_edge - bottom_edge) / (string_count - 1)
    
    # Вычисляем значения функции для всех точек и находим минимальное значение
    y_values = []
    for i in range(string_count):
        x = bottom_edge + i * x_step
        y = func(x)
        y_values.append(y)
    
    min_y = min(y_values)
    
    # Сдвигаем все значения y так, чтобы минимальное значение было равно 0
    y_values_shifted = [y - min_y for y in y_values]
    
    # Вычисляем максимальное значение после сдвига для определения ширины графика
    max_y_shifted = max(y_values_shifted)
    
    # Определяем ширину графика (максимальное количество пробелов)
    # Используем max_y_shifted для определения ширины
    width = int(max_y_shifted) + 1 if max_y_shifted > 0 else 1
    
    # Выводим график
    for i in range(string_count):
        y = y_values_shifted[i]
        # Количество пробелов перед звездочкой равно значению y
        spaces = int(y)
        line = ' ' * spaces + '*'
        print(line)


# Проверка работы функции на примере
def x_2(x):
    return x**2 

print("Пример для функции x_2(x) в диапазоне от -5 до 5 с количеством строк 11:")
draw_symbol_plot(x_2, -5, 5, 11)

# Дополнительные тесты
print("\n\nПример для функции sin(x) в диапазоне от 0 до 3.14 с количеством строк 10:")
import math
def sin_x(x):
    return math.sin(x)
draw_symbol_plot(sin_x, 0, math.pi, 10)

print("\n\nПример для функции линейной функции x в диапазоне от 0 до 10 с количеством строк 11:")
def linear_x(x):
    return x
draw_symbol_plot(linear_x, 0, 10, 11)