#!/usr/bin/env python3

def calculate_patterns(n):
    """
    Calcula el número de patrones diferentes de propagación viral para una distancia dada.
    Implementación iterativa optimizada del algoritmo de Fibonacci con casos base específicos.
    
    Args:
        n: La distancia para la cual calcular los patrones
        
    Returns:
        El número de patrones diferentes
    """
    if n == 0 or n == 1:
        return 1
    
    a, b = 1, 1  # F(0), F(1)
    
    for i in range(2, n + 1):
        a, b = b, a + b
    
    return b
