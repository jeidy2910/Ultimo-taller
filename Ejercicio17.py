import random
import math

def generar_problema_88_17():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
     
        años_mayor = random.randint(10,20)
        veces = random.randint(2,5)
        
        numerador = años_mayor
        denominador = veces - 1
        
        
        
        if numerador % denominador == 0:
            x = numerador // denominador
            
            print("\n" + "=" * 80)
            print("Autor: Jeidy Alexandra Cordoba Gomez ")
            print("Diciembre de 2025")
            print("Ejercicio 88-17")
            print("=" * 80)
            print(f"La edad de A es el triple de la de B, y la de B es {veces} veces la de C. B tiene {años_mayor} años más que C. ¿Qué edad tiene cada uno?")
            print()
            print("Solución paso a paso:")
            print(f"Sea x la edad de C")
            print(f"La edad de B es {veces} veces la de C, es decir: {veces}x")
            print(f"La edad de A es el triple de la de B, es decir: 3({veces}x)")
            print(f"Solucion:")
            print(f"{veces}x = x + {años_mayor}")
            print(f"{veces}x - x = {años_mayor}")
            print(f"{veces - 1}x = {años_mayor}")
            print(f"x = {años_mayor} ÷ {veces - 1}")
            print(f"x = {x}")
            print()
            print("Resultado:")
            print(f"Edad de A: {3 * (veces * x)}")
            print(f"Edad de B: {veces}x = {veces * x}")
            print(f"Edad de C: {x}")
            print()
            print("Comprobación:")
            print(f"La edad de A es el triple de la de B, es decir: {x} + {años_mayor} = {x + años_mayor} ✓")
            print(f"La edad de B es {veces} veces la de C, es decir: {veces}x = {veces * x} ✓")    
            return
                
        intentos += 1
    print("No se pudo generar un problema válido.")

generar_problema_88_17()