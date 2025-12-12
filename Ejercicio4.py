import random
import math

def generar_problema_88_4():
    intentos = 0
    max_intentos = 1000

    while intentos < max_intentos:
        personas_inicial = random.randint(4, 10)
        personas_final = random.randint(2, personas_inicial - 1)
        
      
        if personas_inicial <= personas_final:
            intentos += 1
            continue
            
        adicional = random.randint(1000, 100000)
        adicional = (adicional // 1000) * 1000  
      
        
        numerador = adicional * personas_inicial * personas_final
        denominador = personas_inicial - personas_final
        
        if numerador % denominador == 0:
            x = numerador // denominador
            
            print("\n" + "=" * 80)
            print("Autor: Jeidy Alexandra Cordoba Gomez")
            print("Diciembre de 2025")
            print("Ejercicio 88-4")
            print("=" * 80)
            print("Enunciado:")
            print(f"{personas_inicial} personas iban a comprar una propiedad contribuyendo por partes iguales, "
                  f"pero {personas_inicial - personas_final} de ellas desistieron del negocio y entonces cada una "
                  f"de las {personas_final} restantes tuvo que poner {adicional:,} bolívares más. "
                  f"¿Cuál es el valor de la propiedad?")
            print()
            print("Solución paso a paso:")
            print(f"Sea x el valor de la propiedad.")
            print(f"Inicialmente, {personas_inicial} personas pagarían: x/{personas_inicial} cada una")
            print(f"Finalmente, {personas_final} personas pagan: x/{personas_final} cada una")
            print(f"La diferencia es {adicional:,} bolívares: x/{personas_final} - x/{personas_inicial} = {adicional:,}")
            print()
            print(f"Resolviendo la ecuación:")
            print(f"x/{personas_final} - x/{personas_inicial} = {adicional:,}")
            
            
            mcm = math.lcm(personas_inicial, personas_final)
            factor1 = mcm // personas_final
            factor2 = mcm // personas_inicial
            
            print(f"Mínimo común múltiplo de {personas_inicial} y {personas_final} es {mcm}")
            print(f"{factor1}x/{mcm} - {factor2}x/{mcm} = {adicional:,}")
            print(f"({factor1 - factor2})x/{mcm} = {adicional:,}")
            print(f"x = {adicional:,} × {mcm} / {factor1 - factor2}")
            print(f"x = {x:,} bolívares")
            print()
            print("Resultado final:")
            print(f"Valor de la propiedad: {x:,} bolívares")
            print()
            print("Comprobación:")
            print(f"Cuota inicial: {x:,} / {personas_inicial} = {x // personas_inicial:,}")
            print(f"Cuota final: {x:,} / {personas_final} = {x // personas_final:,}")
            print(f"Diferencia: {x // personas_final - x // personas_inicial:,} = {adicional:,} ✓")
            return
            
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")
    
generar_problema_88_4()