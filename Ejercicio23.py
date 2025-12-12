import random

def generar_problema_88_23():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
        personas_iniciales = random.randint(2, 8)
        personas_extra = random.randint(1, 4)
        ahorro_por_persona = random.randint(100000, 1000000)
    
        
        numerador = ahorro_por_persona * personas_iniciales * (personas_iniciales + personas_extra)
        
        if numerador % personas_extra == 0:
            x = numerador // personas_extra
            
            print("\n" + "=" * 80)
            print("Autor: Jeidy Alexandra Cordoba Gomez ")
            print("Diciembre de 2025")
            print("Ejercicio 88-23")
            print("=" * 80)
            print(f"{personas_iniciales} personas compraron una tienda contribuyendo por partes iguales.")
            print(f"Si tuvieran {personas_extra} socios más, cada uno pagaría {ahorro_por_persona:,} bolívares menos.")
            print(f"¿Cuánto costó la tienda?")
            print()
            
            print("Solución:")
            print(f"Sea x el costo de la tienda")
            print(f"{personas_iniciales} personas contribuyen por partes iguales: x/{personas_iniciales}")
            print(f"Si tuvieran {personas_extra} socios más ({personas_iniciales + personas_extra} personas),")
            print(f"cada uno pagaría: x/{personas_iniciales + personas_extra}")
            print()
            
            print(f"La diferencia es {ahorro_por_persona:,}:")
            print(f"x/{personas_iniciales} - x/{personas_iniciales + personas_extra} = {ahorro_por_persona:,}")
            print()
            
            print(f"Resolviendo:")
            print(f"Mínimo común múltiplo de {personas_iniciales} y {personas_iniciales + personas_extra}:")
            print(f"  = {personas_iniciales} x {personas_iniciales + personas_extra} = {personas_iniciales * (personas_iniciales + personas_extra)}")
            print()
            
            print(f"({personas_iniciales + personas_extra})x/{personas_iniciales*(personas_iniciales + personas_extra)} - {personas_iniciales}x/{personas_iniciales*(personas_iniciales + personas_extra)} = {ahorro_por_persona:,}")
            print(f"[({personas_iniciales + personas_extra})x - {personas_iniciales}x]/{personas_iniciales*(personas_iniciales + personas_extra)} = {ahorro_por_persona:,}")
            print(f"{personas_extra}x/{personas_iniciales*(personas_iniciales + personas_extra)} = {ahorro_por_persona:,}")
            print()
            
            print(f"{personas_extra}x = {ahorro_por_persona:,} × {personas_iniciales*(personas_iniciales + personas_extra)}")
            print(f"{personas_extra}x = {ahorro_por_persona * personas_iniciales * (personas_iniciales + personas_extra):,}")
            print(f"x = {ahorro_por_persona * personas_iniciales * (personas_iniciales + personas_extra):,} ÷ {personas_extra}")
            print(f"x = {x:,} bolívares")
            print()
            
            print(f"Resultado: La tienda costó {x:,} bolívares")
            print()
            
            print(f"Comprobación:")
            print(f"Con {personas_iniciales} personas: {x:,} ÷ {personas_iniciales} = {x//personas_iniciales:,} cada uno")
            print(f"Con {personas_iniciales + personas_extra} personas: {x:,} ÷ {personas_iniciales + personas_extra} = {x//(personas_iniciales + personas_extra):,} cada uno")
            print(f"Diferencia: {x//personas_iniciales - x//(personas_iniciales + personas_extra):,} = {ahorro_por_persona:,} ✓")
            return
                
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")
    
generar_problema_88_23()