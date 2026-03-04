def get_schedule(day, is_odd, scheduled):
    """
    Формирует расписание на указанный день недели.
    
    Args:
        day: номер дня недели (0 - понедельник, 6 - воскресенье)
        is_odd: True для числителя, False для знаменателя
        scheduled: список кортежей с занятиями
        Каждый кортеж: (день, номер_пары, признак_недели, название, преподаватель)
    
    Returns:
        кортеж из 8 строк с расписанием на день
    """
    # Создаем список из 8 пустых строк (максимум 8 пар в день)
    schedule = ['-'] * 8
    
    # Проходим по всем занятиям
    for lesson in scheduled:
        # Распаковываем кортеж
        lesson_day = lesson[0]      # день недели
        lesson_num = lesson[1]       # номер пары (начиная с 0)
        lesson_week = lesson[2]      # признак недели (числитель/знаменатель)
        lesson_name = lesson[3]      # название занятия
        
        # Проверяем, подходит ли занятие для нашего дня и недели
        if lesson_day == day and lesson_week == is_odd:
            # Добавляем занятие в соответствующую пару
            # Используем номер пары как есть, так как в тесте:
            # пара 3 -> позиция 3 в кортеже, но ожидается на позиции 2?
            # Давайте проверим оба варианта
            
            # Вариант 1: используем номер пары как индекс (сдвиг не требуется)
            if 0 <= lesson_num < 8:
                schedule[lesson_num] = lesson_name
            
            # Вариант 2: если нужен сдвиг на -1 (пары нумеруются с 1)
            # if 1 <= lesson_num <= 8:
            #     schedule[lesson_num - 1] = lesson_name
    
    return tuple(schedule)


# Диагностика
if __name__ == "__main__":
    # Тестовые данные из ошибки
    test_scheduled = [
        (4, 3, True, "Программирование - лекция", "Коровченко Игорь Сергеевич"),
        (4, 4, True, "Программирование - практика", "Коровченко Игорь Сергеевич"),
        (4, 5, True, "Программирование - практика", "Коровченко Игорь Сергеевич"),
    ]
    
    result = get_schedule(4, True, test_scheduled)
    print("Результат (без сдвига):")
    print(result)
    print(f"Длина результата: {len(result)}")
    
    # Пробуем со сдвигом на -1
    def get_schedule_with_shift(day, is_odd, scheduled):
        schedule = ['-'] * 8
        for lesson in scheduled:
            if lesson[0] == day and lesson[2] == is_odd:
                # Сдвигаем номер пары на -1 (преобразуем 3->2, 4->3, 5->4)
                lesson_num = lesson[1] - 1
                if 0 <= lesson_num < 8:
                    schedule[lesson_num] = lesson[3]
        return tuple(schedule)
    
    result_shift = get_schedule_with_shift(4, True, test_scheduled)
    print("\nРезультат со сдвигом на -1:")
    print(result_shift)
    
    expected = ('-', '-', 'Программирование - лекция', 'Программирование - практика', 
                'Программирование - практика', '-', '-', '-')
    print("\nОжидаемый результат:")
    print(expected)
    
    if result_shift == expected:
        print("\n✅ Со сдвигом работает правильно!")
    else:
        print("\n❌ Нужна другая корректировка")