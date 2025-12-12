import random
import math

def generar_problema_88_15():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
        
        total_herencia = random.randint(10000000, 50000000)  
        diferencia = random.randint(500000, 5000000)  
        hijos = random.randint(2, 5)  
        hijas = random.randint(1, 4)  
        
        
        
        numerador = total_herencia - hijas * diferencia
        
        if numerador % (hijos + hijas) == 0 and numerador > 0:
            x = numerador // (hijos + hijas) 
            
            if x > 0:
                parte_hija = x + diferencia
                
                print("\n" + "=" * 80)
                print("Autor: Jeidy Alexandra Cordoba Gomez ")
                print("Diciembre de 2025")
                print("Ejercicio 88-15")
                print("=" * 80)
                print(f"Un hombre deja una herencia de {total_herencia:,} colones")
                print(f"para repartir entre {hijos} hijos y {hijas} hijas,")
                print(f"y manda que cada hija reciba {diferencia:,} más que cada hijo.")
                print(f"Hallar la parte de cada hijo e hija.")
                print()
                
                print("Solución:")
                print(f"Sea x = parte de cada hijo")
                print(f"Cada hija recibe: x + {diferencia:,}")
                print()
                print(f"Total hijos: {hijos}x")
                print(f"Total hijas: {hijas}(x + {diferencia:,})")
                print()
                print(f"Ecuación: {hijos}x + {hijas}(x + {diferencia:,}) = {total_herencia:,}")
                print(f"{hijos}x + {hijas}x + {hijas*diferencia:,} = {total_herencia:,}")
                print(f"({hijos + hijas})x = {total_herencia:,} - {hijas*diferencia:,}")
                print(f"({hijos + hijas})x = {numerador:,}")
                print(f"x = {numerador:,} ÷ {hijos + hijas}")
                print(f"x = {x:,} (cada hijo)")
                print()
                print(f"Cada hija: {x:,} + {diferencia:,} = {parte_hija:,}")
                print()
                print(f"Resultado:")
                print(f"Cada hijo recibe: {x:,} colones")
                print(f"Cada hija recibe: {parte_hija:,} colones")
                print()
                print(f"Comprobación:")
                print(f"Hijos: {hijos} × {x:,} = {hijos*x:,}")
                print(f"Hijas: {hijas} × {parte_hija:,} = {hijas*parte_hija:,}")
                print(f"Total: {hijos*x:,} + {hijas*parte_hija:,} = {hijos*x + hijas*parte_hija:,}")
                print(f"Herencia: {total_herencia:,} ✓")
                return
                
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")
    
generar_problema_88_15()