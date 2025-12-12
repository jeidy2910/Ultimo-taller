import random
import math

def generar_problema_88_5():
    intentos = 0
    max_intentos = 1000

    while intentos < max_intentos:
        total = random.randint(50, 500)
        
        excede = random.randint(10, 200)
        
     
        
        numerador = 2 * total - excede
        
        if numerador > 0 and numerador % 5 == 0:
            x = numerador // 5
            if x > 0 and x < total:
                mayor = total - x
                
                print("\n" + "=" * 80)
                print("Autor: Jeidy Alexandra Cordoba Gomez")
                print("Diciembre de 2025")
                print("Ejercicio 88-5")
                print("=" * 80)
                print("Enunciado:")
                print(f"La suma de dos números es {total} y el doble del mayor excede al triple del menor en {excede}. Hallar los números.")
                print()
                print("Solución paso a paso:")
                print(f"Sea x el número menor.")
                print(f"Entonces {total} - x es el número mayor.")
                print(f"El doble del mayor excede al triple del menor en {excede}, entonces:")
                print(f"2({total} - x) = 3x + {excede}")
                print(f"Resolviendo:")
                print(f"{2*total} - 2x = 3x + {excede}")
                print(f"{2*total} - {excede} = 3x + 2x")
                print(f"{2*total - excede} = 5x")
                print(f"x = {2*total - excede} ÷ 5 = {x}")
                print(f"Mayor = {total} - {x} = {mayor}")
                print()
                print("Resultado final:")
                print(f"Número menor: {x}")
                print(f"Número mayor: {mayor}")
                print()
                print("Comprobación:")
                print(f"Suma: {x} + {mayor} = {total} ✓")
                print(f"Doble del mayor: 2 X {mayor} = {2*mayor}")
                print(f"Triple del menor: 3 X {x} = {3*x}")
                print(f"Diferencia: {2*mayor} - {3*x} = {2*mayor - 3*x} = {excede} ✓")
                return
                
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")
    
generar_problema_88_5()