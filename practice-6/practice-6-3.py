import random

def monte_carlo_integration(func, a, b, n):
    total = 0.0
    
    for _ in range(n):
        x = random.uniform(a, b)
        total += func(x)
    
    average = total / n
    integral = (b - a) * average
    
    return integral