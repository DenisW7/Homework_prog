def trapezoid_integration(func, a, b, n):
    delta_x = (b - a) / n
    integral = (func(a) + func(b)) / 2.0
    
    for i in range(1, n):
        x = a + i * delta_x
        integral += func(x)
    
    integral *= delta_x
    return integral