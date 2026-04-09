import sys

def adaptive_integration(integration_func, func, a, b, tol, max_depth=20):
    sys.setrecursionlimit(10000)
    
    m = (a + b) / 2
    
    whole = integration_func(func, a, b, 1)
    left = integration_func(func, a, m, 1)
    right = integration_func(func, m, b, 1)
    
    if abs(left + right - whole) < tol or max_depth <= 0:
        return left + right
    
    return (adaptive_integration(integration_func, func, a, m, tol / 2, max_depth - 1) +
            adaptive_integration(integration_func, func, m, b, tol / 2, max_depth - 1))


def rectangle_integration(func, a, b, n):
    delta_x = (b - a) / n
    integral = 0.0
    
    for i in range(n):
        x = a + i * delta_x
        integral += func(x) * delta_x
    
    return integral


def trapezoid_integration(func, a, b, n):
    delta_x = (b - a) / n
    integral = (func(a) + func(b)) / 2.0
    
    for i in range(1, n):
        x = a + i * delta_x
        integral += func(x)
    
    integral *= delta_x
    return integral