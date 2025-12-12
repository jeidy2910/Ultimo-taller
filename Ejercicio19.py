import random

def generar_problema_88_19():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
        
        
        total_ganado = random.randint(500, 2000)
        factor = random.randint(2, 3)
        
        resta_viernes = random.randint(10, 100)
        suma_sabado = random.randint(5, 50)
        
   
        
        suma_coeficientes = 1 + factor + factor**2 + 3*factor**3
        numerador = total_ganado + 2*resta_viernes - suma_sabado
        
        if suma_coeficientes != 0 and numerador % suma_coeficientes == 0:
            x = numerador // suma_coeficientes
            
            
            
            lunes = x
            martes = factor * x
            miercoles = factor**2 * x
            jueves = factor**3 * x
            viernes = jueves - resta_viernes
            sabado = viernes + suma_sabado
            
            
            if all(ganado > 0 for ganado in [lunes, martes, miercoles, jueves, viernes, sabado]):
                print("\n" + "=" * 80)
                print("Autor: Jeidy Alexandra Cordoba Gomez ")
                print("Diciembre de 2025")
                print("Ejercicio 88-19")
                print("=" * 80)
                print(f"Un hombre ganó una cantidad de dinero durante 6 días.")
                print(f"Cada día ganó {factor} veces lo del día anterior,")
                print(f"excepto el viernes que ganó ${resta_viernes} menos que el jueves,")
                print(f"y el sábado ganó ${suma_sabado} más que el viernes.")
                print(f"En total ganó ${total_ganado}. ¿Cuánto ganó el lunes?")
                print()
                
                print("Solución:")
                print(f"Sea x lo que ganó el lunes")
                print()
                print(f"Martes: {factor}x (ganó {factor} veces lo del lunes)")
                print(f"Miércoles: {factor}×{factor}x = {factor**2}x (ganó {factor} veces lo del martes)")
                print(f"Jueves: {factor}×{factor**2}x = {factor**3}x (ganó {factor} veces lo del miércoles)")
                print(f"Viernes: {factor**3}x - {resta_viernes} (ganó ${resta_viernes} menos que el jueves)")
                print(f"Sábado: ({factor**3}x - {resta_viernes}) + {suma_sabado} = {factor**3}x - {resta_viernes - suma_sabado}")
                print()
                
                print(f"Suma total = ${total_ganado}:")
                print(f"x + {factor}x + {factor**2}x + {factor**3}x + ({factor**3}x - {resta_viernes}) + ({factor**3}x - {resta_viernes - suma_sabado}) = {total_ganado}")
                print(f"x + {factor}x + {factor**2}x + {factor**3}x + {factor**3}x - {resta_viernes} + {factor**3}x - {resta_viernes - suma_sabado} = {total_ganado}")
                print(f"(1 + {factor} + {factor**2} + {factor**3} + {factor**3} + {factor**3})x - {2*resta_viernes - suma_sabado} = {total_ganado}")
                print(f"{suma_coeficientes}x = {total_ganado} + {2*resta_viernes - suma_sabado}")
                print(f"{suma_coeficientes}x = {numerador}")
                print(f"x = {numerador} ÷ {suma_coeficientes}")
                print(f"x = ${x}")
                print()
                
                print(f"Resultado: Ganó ${x} el lunes")
                print()
                print(f"Comprobación:")
                print(f"Lunes: ${lunes}")
                print(f"Martes: ${martes} ({factor}×{lunes})")
                print(f"Miércoles: ${miercoles} ({factor}×{martes})")
                print(f"Jueves: ${jueves} ({factor}×{miercoles})")
                print(f"Viernes: ${viernes} (${jueves} - ${resta_viernes})")
                print(f"Sábado: ${sabado} (${viernes} + ${suma_sabado})")
                print(f"Total: ${lunes + martes + miercoles + jueves + viernes + sabado} = ${total_ganado} ✓")
                return
                
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")

generar_problema_88_19()