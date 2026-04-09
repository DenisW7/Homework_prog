def linear_search(target, arr):
    """
    Производит линейный поиск элемента в списке

    :param target (int): элемент, который нужно найти
    :param arr (list of int): список элементов, в котором осуществляется поиск
    :return (int): индекс найденного элемента или -1, если элемент не найден
    """
    # Проходим по всем элементам списка с их индексами
    for index, element in enumerate(arr):
        # Если текущий элемент равен искомому
        if element == target:
            return index  # Возвращаем индекс первого вхождения
    
    # Если элемент не найден после проверки всех элементов
    return -1


# Функция для тестирования с выводом результатов
def test_linear_search():
    """
    Тестирование функции linear_search на различных случаях
    """
    print("=" * 50)
    print("ТЕСТИРОВАНИЕ ЛИНЕЙНОГО ПОИСКА")
    print("=" * 50)
    
    # Тест 1: пустой массив
    print("\nТест 1: Пустой массив")
    arr1 = []
    target1 = 10
    result1 = linear_search(target1, arr1)
    print(f"Массив: {arr1}")
    print(f"Искомый элемент: {target1}")
    print(f"Результат: {result1}")
    assert result1 == -1, "Ошибка: должен вернуть -1"
    print("✓ Тест пройден")
    
    # Тест 2: массив с одним элементом (искомый присутствует)
    print("\nТест 2: Массив с одним элементом (присутствует)")
    arr2 = [42]
    target2 = 42
    result2 = linear_search(target2, arr2)
    print(f"Массив: {arr2}")
    print(f"Искомый элемент: {target2}")
    print(f"Результат: {result2}")
    assert result2 == 0, "Ошибка: должен вернуть 0"
    print("✓ Тест пройден")
    
    # Тест 3: массив с одним элементом (искомый отсутствует)
    print("\nТест 3: Массив с одним элементом (отсутствует)")
    arr3 = [42]
    target3 = 100
    result3 = linear_search(target3, arr3)
    print(f"Массив: {arr3}")
    print(f"Искомый элемент: {target3}")
    print(f"Результат: {result3}")
    assert result3 == -1, "Ошибка: должен вернуть -1"
    print("✓ Тест пройден")
    
    # Тест 4: обычный массив, элемент найден
    print("\nТест 4: Обычный массив (элемент найден)")
    arr4 = [10, 20, 30, 40, 50]
    target4 = 30
    result4 = linear_search(target4, arr4)
    print(f"Массив: {arr4}")
    print(f"Искомый элемент: {target4}")
    print(f"Результат: {result4}")
    assert result4 == 2, "Ошибка: должен вернуть 2"
    print("✓ Тест пройден")
    
    # Тест 5: элемент не найден
    print("\nТест 5: Обычный массив (элемент не найден)")
    arr5 = [10, 20, 30, 40, 50]
    target5 = 100
    result5 = linear_search(target5, arr5)
    print(f"Массив: {arr5}")
    print(f"Искомый элемент: {target5}")
    print(f"Результат: {result5}")
    assert result5 == -1, "Ошибка: должен вернуть -1"
    print("✓ Тест пройден")
    
    # Тест 6: повторяющиеся элементы (возвращает первое вхождение)
    print("\nТест 6: Массив с повторяющимися элементами")
    arr6 = [5, 3, 7, 3, 9, 3, 1]
    target6 = 3
    result6 = linear_search(target6, arr6)
    print(f"Массив: {arr6}")
    print(f"Искомый элемент: {target6}")
    print(f"Результат: {result6} (первое вхождение на индексе 1)")
    assert result6 == 1, "Ошибка: должен вернуть 1 (первое вхождение)"
    print("✓ Тест пройден")
    
    # Тест 7: элемент в начале массива
    print("\nТест 7: Элемент в начале массива")
    arr7 = [1, 2, 3, 4, 5]
    target7 = 1
    result7 = linear_search(target7, arr7)
    print(f"Массив: {arr7}")
    print(f"Искомый элемент: {target7}")
    print(f"Результат: {result7}")
    assert result7 == 0, "Ошибка: должен вернуть 0"
    print("✓ Тест пройден")
    
    # Тест 8: элемент в конце массива
    print("\nТест 8: Элемент в конце массива")
    arr8 = [1, 2, 3, 4, 5]
    target8 = 5
    result8 = linear_search(target8, arr8)
    print(f"Массив: {arr8}")
    print(f"Искомый элемент: {target8}")
    print(f"Результат: {result8}")
    assert result8 == 4, "Ошибка: должен вернуть 4"
    print("✓ Тест пройден")
    
    # Тест 9: большой массив
    print("\nТест 9: Большой массив (1000 элементов)")
    arr9 = list(range(1000))
    target9 = 999
    result9 = linear_search(target9, arr9)
    print(f"Искомый элемент: {target9}")
    print(f"Результат: {result9}")
    assert result9 == 999, "Ошибка: должен вернуть 999"
    print("✓ Тест пройден")
    
    print("\n" + "=" * 50)
    print("ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ! ✓")
    print("=" * 50)


# Пример использования из задания
if __name__ == "__main__":
    # Пример из задания
    print("ПРИМЕР ИСПОЛЬЗОВАНИЯ:")
    print("-" * 30)
    array = [10, 20, 30, 40, 50]
    target = 30
    result = linear_search(target, array)
    
    if result != -1:
        print(f"Элемент {target} найден на позиции {result}.")
    else:
        print(f"Элемент {target} в списке не найден.")
    
    print("\n")
    
    # Запуск всех тестов
    test_linear_search()
    
    # Дополнительный пример с разными типами данных
    print("\nДОПОЛНИТЕЛЬНЫЙ ПРИМЕР:")
    print("-" * 30)
    # Функция работает с любыми типами данных, поддерживающими сравнение
    mixed_array = ["apple", "banana", "cherry", "date", "elderberry"]
    target_fruit = "cherry"
    result_fruit = linear_search(target_fruit, mixed_array)
    
    if result_fruit != -1:
        print(f"Элемент '{target_fruit}' найден на позиции {result_fruit}.")
    else:
        print(f"Элемент '{target_fruit}' в списке не найден.")