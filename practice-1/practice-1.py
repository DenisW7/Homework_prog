def get_calendar(week, first, count):
    # Находим индекс первого дня недели в списке week
    first_index = week.index(first)
    
    # Создаем календарь с заголовком (дни недели)
    calendar = [week[:]]
    
    # Определяем количество пустых ячеек перед первым днем
    empty_cells = first_index
    
    # Создаем строки календаря
    day = 1
    current_row = []
    
    # Добавляем пустые ячейки для начала месяца
    for _ in range(empty_cells):
        current_row.append("  ")
    
    # Заполняем дни месяца
    while day <= count:
        # Форматируем день: добавляем пробел для чисел 1-9
        formatted_day = f"{day:2d}"
        current_row.append(formatted_day)
        day += 1
        
        # Если строка заполнена (7 дней), добавляем её в календарь и начинаем новую
        if len(current_row) == 7:
            calendar.append(current_row)
            current_row = []
    
    # Добавляем пустые ячейки в последнюю строку, если она неполная
    if current_row:
        while len(current_row) < 7:
            current_row.append("  ")
        calendar.append(current_row)
    
    return calendar

week = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"]
calendar = get_calendar(week, "ЧТ", 29)

for row in calendar:
    print(row)