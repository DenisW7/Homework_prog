def draw_symbol_plot(func, bottom_edge, top_edge, string_count):
    step = (top_edge - bottom_edge) / (string_count - 1)
    
    y_values = []
    
    for i in range(string_count):
        x = bottom_edge + i * step
        y_values.append(func(x))
    
    min_y = min(y_values)
    max_y = max(y_values)
    
    height = int(round(max_y - min_y)) + 1
    
    for row_index in range(height - 1, -1, -1):
        line = []
        for i in range(string_count):
            y_adjusted = y_values[i] - min_y
            row = int(round(y_adjusted))
            if row == row_index:
                line.append('*')
            else:
                line.append(' ')
        print(''.join(line))