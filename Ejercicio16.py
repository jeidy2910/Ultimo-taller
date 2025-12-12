import random
import math


def generar_problema_88_16():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
      
        diferencia = random.randint(10, 200)
        
        salto = random.randint(1, 5)  
        
       
        
        numerador = diferencia - salto**2
        denominador = 2 * salto
        
        if denominador != 0 and numerador % denominador == 0 and numerador > 0:
            x = numerador // denominador
            
            if x > 0:
                numero1 = x
                numero2 = x + salto
                
                print("\n" + "=" * 80)
                print("Autor: Jeidy Alexandra Cordoba Gomez ")
                print("Diciembre de 2025")
                print("Ejercicio 88-16")
                print("=" * 80)
                print(f"La diferencia de los cuadrados de dos números enteros que difieren en {salto} es {diferencia}.")
                print(f"Hallar los números.")
                print()
                
                print("Solución:")
                print(f"Sea x el primer número")
                print(f"La diferencia es {diferencia}")
                print(f"La suma de los cuadrados es {(numero1 + numero2)**2}")
                print(f"El número entero consecutivo mayor es x + {salto}, entonces su cuadrado es (x + {salto})^2")
                print(f"(x + {salto})² - x² = {diferencia}")
                print(f"x² + {2*salto}x + {salto**2} - x² = {diferencia}")
                print(f"{2*salto}x + {salto**2} = {diferencia}")
                print(f"{2*salto}x = {diferencia} - {salto**2}")
                print(f"{2*salto}x = {numerador}")
                print(f"x = {numerador} ÷ {2*salto}")
                print(f"x = {numero1}")
                print()
                print(f"Números: {numero1} y {numero2}")
                return
                
        intentos += 1
    print("No se pudo generar un problema válido.")


generar_problema_88_16()