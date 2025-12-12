import random

def generar_problema_88_29():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
        primer_gasto = random.randint(10, 100)
        segundo_gasto = random.randint(100, 500)
        
        numerador = 3 * primer_gasto + segundo_gasto
        
        if numerador % 6 == 0:
            x = numerador // 6
            
            if x > 0:
                print("\n" + "=" * 80)
                print("Autor: Jeidy Alexandra Cordoba Gomez ")
                print("Diciembre de 2025")
                print("Ejercicio 88-29")
                print("=" * 80)
                print(f"Tenía cierta suma de dinero. Ahorré una suma igual a lo que tenía")
                print(f"y gasté {primer_gasto} nuevos soles; luego ahorré una suma igual")
                print(f"al doble de lo que me quedaba y gasté {segundo_gasto} nuevos soles.")
                print(f"Si ahora no tengo nada, ¿cuánto tenía al principio?")
                print()
                
                print("Solución:")
                print(f"Sea x lo que tenía al principio")
                print()
                print(f"1. Ahorré una suma igual a lo que tenía: x + x = 2x")
                print(f"2. Gasté {primer_gasto}: queda = 2x - {primer_gasto}")
                print()
                print(f"3. Ahorré el doble de lo que me quedaba: 2(2x - {primer_gasto})")
                print(f"4. Ahora tengo: 2(2x - {primer_gasto}) + (2x - {primer_gasto})")
                print(f"   = 4x - {2*primer_gasto} + 2x - {primer_gasto}")
                print(f"   = 6x - {3*primer_gasto}")
                print(f"5. Gasté {segundo_gasto}: queda = 6x - {3*primer_gasto} - {segundo_gasto}")
                print()
                print(f"Como ahora no tengo nada:")
                print(f"6x - {3*primer_gasto} - {segundo_gasto} = 0")
                print(f"6x = {3*primer_gasto + segundo_gasto}")
                print(f"6x = {numerador}")
                print(f"x = {numerador} ÷ 6")
                print(f"x = {x}")
                print()
                
                print(f"Resultado: Tenía al principio {x} nuevos soles")
                print()
                
                print(f"Comprobación paso a paso:")
                print(f"1. Tenía: {x}")
                print(f"2. Ahorro igual: +{x} → Total: {2*x}")
                print(f"3. Gasto {primer_gasto} → Queda: {2*x - primer_gasto}")
                print(f"4. Ahorro el doble: +{2*(2*x - primer_gasto)} → Total: {2*(2*x - primer_gasto) + (2*x - primer_gasto)}")
                print(f"   Simplificado: 6x - {3*primer_gasto} = {6*x - 3*primer_gasto}")
                print(f"5. Gasto {segundo_gasto} → Queda: {6*x - 3*primer_gasto - segundo_gasto}")
                print(f"6. Verificación: {6*x - 3*primer_gasto - segundo_gasto} = 0")
                return          
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")
    
generar_problema_88_29()