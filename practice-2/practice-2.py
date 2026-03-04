def get_schedule(day, is_odd, scheduled):
    schedule = ['-'] * 8
    
    # Проходим по всем занятиям
    for lesson in scheduled:
        # Проверяем, подходит ли занятие для нашего дня и недели
        if lesson['day'] == day and lesson['is_odd'] == is_odd:
            # Добавляем занятие в соответствующую пару
            schedule[lesson['lesson']] = lesson['name']
    
    return tuple(schedule)


# Пример использования:
if __name__ == "__main__":
    # Пример данных в формате словарей
    scheduled = [
        {'day': 0, 'lesson': 0, 'is_odd': True, 'name': 'Физическая культура'},
        {'day': 0, 'lesson': 0, 'is_odd': False, 'name': 'Физическая культура'},
        {'day': 0, 'lesson': 1, 'is_odd': True, 'name': 'История России - лекция'},
        {'day': 0, 'lesson': 1, 'is_odd': False, 'name': 'История России - лекция'},
        {'day': 0, 'lesson': 2, 'is_odd': True, 'name': 'Физика - практика'},
        {'day': 1, 'lesson': 0, 'is_odd': True, 'name': 'Физика - лекция'},
        {'day': 1, 'lesson': 0, 'is_odd': False, 'name': 'Физика - лекция'},
        {'day': 2, 'lesson': 0, 'is_odd': True, 'name': 'Физическая культура'},
        {'day': 2, 'lesson': 0, 'is_odd': False, 'name': 'Физическая культура'},
        {'day': 3, 'lesson': 0, 'is_odd': True, 'name': 'Математический анализ - лекция'},
        {'day': 3, 'lesson': 0, 'is_odd': False, 'name': 'Математический анализ - лекция'},
        {'day': 3, 'lesson': 1, 'is_odd': True, 'name': 'История России - практика'},
        {'day': 3, 'lesson': 1, 'is_odd': False, 'name': 'История России - практика'},
        {'day': 3, 'lesson': 2, 'is_odd': True, 'name': 'Математический анализ - практика'},
        {'day': 3, 'lesson': 2, 'is_odd': False, 'name': 'Математический анализ - практика'},
        {'day': 3, 'lesson': 5, 'is_odd': True, 'name': 'Информационные технологии - практика'},
        {'day': 3, 'lesson': 5, 'is_odd': False, 'name': 'Информационные технологии - практика'},
        {'day': 4, 'lesson': 0, 'is_odd': True, 'name': 'Деловое общение и культура речи'},
        {'day': 4, 'lesson': 1, 'is_odd': True, 'name': 'Деловое общение и культура речи'},
        {'day': 4, 'lesson': 0, 'is_odd': False, 'name': 'Физика - лабораторная работа'},
        {'day': 4, 'lesson': 1, 'is_odd': False, 'name': 'Физика - лабораторная работа'},
        {'day': 4, 'lesson': 2, 'is_odd': True, 'name': 'Английский язык'},
        {'day': 4, 'lesson': 2, 'is_odd': False, 'name': 'Английский язык'},
        {'day': 4, 'lesson': 3, 'is_odd': False, 'name': 'Физика - лабораторная работа'},
        {'day': 4, 'lesson': 4, 'is_odd': False, 'name': 'Физика - лабораторная работа'},
        {'day': 4, 'lesson': 5, 'is_odd': True, 'name': 'Программирование - практика'},
        {'day': 4, 'lesson': 6, 'is_odd': True, 'name': 'Программирование - практика'},
        {'day': 4, 'lesson': 5, 'is_odd': False, 'name': 'Программирование - практика'},
        {'day': 4, 'lesson': 6, 'is_odd': False, 'name': 'Программирование - практика'},
        {'day': 5, 'lesson': 1, 'is_odd': True, 'name': 'Информационные технологии - лекция'},
        {'day': 5, 'lesson': 2, 'is_odd': True, 'name': 'Дискретная математика - лекция'},
        {'day': 5, 'lesson': 3, 'is_odd': True, 'name': 'Дискретная математика - практика'},
        {'day': 5, 'lesson': 1, 'is_odd': False, 'name': 'Информационные технологии - лекция'},
        {'day': 5, 'lesson': 2, 'is_odd': False, 'name': 'Дискретная математика - лекция'},
        {'day': 5, 'lesson': 3, 'is_odd': False, 'name': 'Дискретная математика - практика'}
    ]
    
    # Получаем расписание для пятницы (day=4) по знаменателю (is_odd=False)
    result = get_schedule(4, False, scheduled)
    
    # Выводим результат
    print("Расписание на пятницу (знаменатель):")
    print(result)
    