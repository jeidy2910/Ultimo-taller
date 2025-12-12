import random
import math

def generar_problema_88_14():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
       
        totalKm = random.randint(100, 1000)
        multiplicador = random.randint(2, 5)
        KmMenos = random.randint(1, 30)
        
       
        
        numerador = totalKm - KmMenos
        denominador = multiplicador + 2
        if numerador % denominador == 0:
            x = numerador // denominador
            if x > 0:
                print("\n" + "=" * 80)
                print("Autor: Jeidy Alexandra Cordoba Gomez ")
                print("Diciembre de 2025")
                print("Ejercicio 88-14")
                print("=" * 80)
                print(f"")
                print(f"Un hombre ha recorrido {totalKm} kilómetros. En auto recorrió una distancia {multiplicador} veces mayot")
                print(f"que la distancia recorrida a caballo y a pie {KmMenos} kilómetros menos que a caballo. ¿Cuánto ha recorrido en cada modo?")
                print()
                print("Solución:")
                print(f"Sea x el número de kilómetros recorridos a caballo")
                print(f"La distancia recorrida en auto es {multiplicador}x")
                print(f"La distancia recorrida a pie es x - {KmMenos}")
                print(f"Total: {totalKm}")
                print(f"Ecuación: x + {multiplicador}x + x - {KmMenos} = {totalKm}")
                print(f"Desarrollando: {multiplicador + 2}x = {totalKm} - {KmMenos}")
                print(f"x = ({totalKm} - {KmMenos}) / {multiplicador + 2}")
                print(f"x = ({totalKm - KmMenos}) / {multiplicador + 2}")
                print(f"x = {(totalKm - KmMenos) / (multiplicador + 2)}")
                print()
                print(f"Resultado: En auto recorrió {x} kilómetros, en caballo {x+multiplicador} kilómetros")
                print(f"y en pie {x-multiplicador} kilómetros")
                return
                
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")

generar_problema_88_14()