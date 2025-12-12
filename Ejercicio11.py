import random
import math

def generar_problema_88_11():
    intentos = 0
    max_intentos = 1000
    while intentos < max_intentos:
        total_caballos = random.randint(10, 40)
        caballos_extra = random.randint(1, 10)
        ahorro_por_caballo = random.randint(100, 1000)  
        
        
        numerador = (total_caballos + caballos_extra) * ahorro_por_caballo
        
        if numerador % caballos_extra == 0:
            precio_por_caballo = numerador // caballos_extra
            
            print("\n" + "=" * 80)
            print("Autor: Jeidy Alexandra Cordoba Gomez ")
            print("Diciembre de 2025")
            print("Ejercicio 88-11")
            print("=" * 80)
            print(f"Un hacendado compró {total_caballos} caballos. Si hubiera comprado {caballos_extra} caballos más")
            print(f"por el mismo precio, cada caballo le costaría ${ahorro_por_caballo} menos.")
            print("¿Cuánto pagó por cada caballo?")
            print()
            print("Solución:")
            print(f"Sea x = precio por caballo")
            print(f"Ecuación: {total_caballos}x = {total_caballos + caballos_extra}(x - {ahorro_por_caballo})")
            print(f"{total_caballos}x = {total_caballos + caballos_extra}x - {(total_caballos + caballos_extra)*ahorro_por_caballo}")
            print(f"{total_caballos}x - {total_caballos + caballos_extra}x = - {(total_caballos + caballos_extra)*ahorro_por_caballo}")
            print(f"{caballos_extra}x = {(total_caballos + caballos_extra)*ahorro_por_caballo}")
            print(f"x = {precio_por_caballo}")
            print()
            print(f"Resultado: Pagó ${precio_por_caballo} por cada caballo")
            return
                
        intentos += 1
    print("No se pudo generar un problema válido.")
    
generar_problema_88_11()