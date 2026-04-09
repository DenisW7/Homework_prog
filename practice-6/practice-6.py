def rectangle_integration(func, a, b, n):
    delta_x = (b - a) / n
    integral = 0.0
    
    for i in range(n):
        x = a + i * delta_x
        integral += func(x) * delta_x
    
    return integral