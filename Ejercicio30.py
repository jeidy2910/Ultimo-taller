import random

def generar_problema_88_30():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
        relacion_largo_ancho = random.randint(2, 4)
        disminucion_largo = random.randint(2, 10)
        aumento_ancho = random.randint(2, 10)
        
        a = aumento_ancho
        d = disminucion_largo
        r = relacion_largo_ancho
        
        numerador = a * d
        denominador = r * a - d
        
        if denominador > 0 and numerador % denominador == 0:
            x = numerador // denominador
          
            if x > 0 and r*x - d > 0:
                ancho = x
                largo = r * x
                nuevo_ancho = ancho + a
                nuevo_largo = largo - d
                
                if ancho * largo == nuevo_ancho * nuevo_largo:
                    print("\n" + "=" * 80)
                    print("Autor: Jeidy Alexandra Cordoba Gomez ")
                    print("Diciembre de 2025")
                    print("Ejercicio 88-30")
                    print("=" * 80)
                    print(f"Una sala tiene {r} veces más de largo que de ancho.")
                    print(f"Si el largo se disminuye en {d} m y el ancho se aumenta en {a} m,")
                    print(f"la superficie de la sala no varía.")
                    print(f"Hallar las dimensiones de la sala.")
                    print()
                    
                    print("Solución:")
                    print(f"Sea x el ancho de la sala")
                    print(f"Largo = {r} x ancho = {r}x")
                    print()
                    print(f"Superficie original: ancho x largo = x x {r}x = {r}x²")
                    print()
                    print(f"Nuevas dimensiones:")
                    print(f"  Ancho: x + {a}")
                    print(f"  Largo: {r}x - {d}")
                    print(f"  Nueva superficie: (x + {a})({r}x - {d})")
                    print()
                    print(f"Como la superficie no varía:")
                    print(f"{r}x² = (x + {a})({r}x - {d})")
                    print(f"{r}x² = {r}x² - {d}x + {r*a}x - {a*d}")
                    print(f"{r}x² = {r}x² + ({r*a - d})x - {a*d}")
                    print(f"0 = ({r*a - d})x - {a*d}")
                    print(f"({r*a - d})x = {a*d}")
                    print(f"x = {a*d} ÷ {r*a - d}")
                    print(f"x = {ancho} m (ancho)")
                    print()
                    print(f"Largo = {r} x {ancho} = {largo} m")
                    print()
                    print(f"Resultado:")
                    print(f"Ancho: {ancho} m")
                    print(f"Largo: {largo} m")
                    print(f"Superficie: {ancho} x {largo} = {ancho*largo} m²")
                    print()
                    print(f"Comprobación:")
                    print(f"Nuevo ancho: {ancho} + {a} = {nuevo_ancho} m")
                    print(f"Nuevo largo: {largo} - {d} = {nuevo_largo} m")
                    print(f"Nueva superficie: {nuevo_ancho} x {nuevo_largo} = {nuevo_ancho*nuevo_largo} m²")
                    print(f"Ambas superficies son iguales: {ancho*largo} = {nuevo_ancho*nuevo_largo} ✓")
                    return
                
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")
    
generar_problema_88_30()