def calc_parser(expression):
    """
    Разбирает строку с арифметическим выражением вида "операнд1 оператор операнд2"
    и возвращает строку с результатом в формате "операнд1 оператор операнд2 = результат"
    """
    # Разделяем строку на части
    parts = expression.split()
    
    # Проверяем, что строка содержит 3 части (операнд1, оператор, операнд2)
    if len(parts) != 3:
        return "Ошибка: неверный формат выражения"
    
    operand1, operator, operand2 = parts
    
    # Преобразуем операнды в числа
    try:
        num1 = float(operand1)
        num2 = float(operand2)
    except ValueError:
        return "Ошибка: операнды должны быть числами"
    
    # Выполняем соответствующую операцию
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Ошибка: деление на ноль"
        result = num1 / num2
    else:
        return f"Ошибка: неподдерживаемый оператор '{operator}'"
    
    # Возвращаем результат в нужном формате
    # Для целых чисел убираем .0
    if result.is_integer():
        result = int(result)
    
    return f"{operand1} {operator} {operand2} = {result}"


# Примеры использования
if __name__ == "__main__":
    # Тестовые примеры
    test_expressions = [
        "5 + 8",
        "10 - 3",
        "4 * 7",
        "15 / 3",
        "7.5 + 2.3",
        "10 / 0",  # Деление на ноль
        "5 + a",   # Не число
        "5+8",     # Нет пробелов
    ]
    
    for expr in test_expressions:
        print(f"Вход: '{expr}'")
        print(f"Выход: {calc_parser(expr)}")
        print("-" * 30)