#!/usr/bin/env python3
from algorithm import calculate_patterns
import time

def main():
    # Calcular el resultado para n = 91
    start_time = time.time()
    result = calculate_patterns(91)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    
    print(f"Resultado para n = 91: {result}")
    print(f"Tiempo de ejecución: {execution_time_ms:.2f} ms")
    
    # Verificar con los ejemplos de prueba
    print("\nVerificación con ejemplos de prueba:")
    print(f"n = 3: {calculate_patterns(3)}")
    print(f"n = 10: {calculate_patterns(10)}")
    print(f"n = 20: {calculate_patterns(20)}")
    print(f"n = 50: {calculate_patterns(50)}")

if __name__ == "__main__":
    main()
