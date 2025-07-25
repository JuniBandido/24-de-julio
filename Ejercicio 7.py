def pedir_lista_reales():
    while True:
        try:
            n = int(input("¿Cuántos números deseas ingresar? "))
            if n <= 0:
                print("Debe ser un número positivo.")
                continue
            lista = []
            for i in range(n):
                num = float(input(f"Ingrese el número {i + 1}: "))
                lista.append(num)
            return lista
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")

def suma_total(lista):
    return sum(lista)

def promedio(lista):
    return sum(lista) / len(lista)

def contar_signos(lista):
    positivos = sum(1 for x in lista if x > 0)
    negativos = sum(1 for x in lista if x < 0)
    ceros = sum(1 for x in lista if x == 0)
    return positivos, negativos, ceros

def multiplos_de_tres(lista):
    return sum(1 for x in lista if x % 3 == 0)

def area_rectangulo(base, altura):
    return base * altura

def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def pedir_calificaciones():
    while True:
        try:
            n = int(input("¿Cuántas calificaciones desea ingresar? "))
            if n <= 0:
                print("Debe ser un número positivo.")
                continue
            calificaciones = []
            for i in range(n):
                nota = float(input(f"Calificación {i + 1}: "))
                if 0 <= nota <= 100:
                    calificaciones.append(nota)
                else:
                    print("Debe estar entre 0 y 100.")
                    return []
            return calificaciones
        except ValueError:
            print("Entrada inválida.")

def analizar_calificaciones(lista):
    promedio_cali = promedio(lista)
    altas = sum(1 for x in lista if x >= 85)
    riesgo = sum(1 for x in lista if x < 60)
    return promedio_cali, altas, riesgo

def pedir_lista_enteros():
    while True:
        try:
            n = int(input("¿Cuántos números enteros deseas ingresar? "))
            if n <= 0:
                print("Debe ser un número positivo.")
                continue
            lista = []
            for i in range(n):
                num = int(input(f"Número {i + 1}: "))
                lista.append(num)
            return lista
        except ValueError:
            print("Entrada inválida.")

def mayor(lista):
    return max(lista)

def menor(lista):
    return min(lista)

def frecuencia(lista):
    from collections import Counter
    frec = Counter(lista)
    return frec

def calculadora():
    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        operacion = input("Operación (+, -, *, /): ")
        if operacion == '+':
            return f"Resultado: {a + b}"
        elif operacion == '-':
            return f"Resultado: {a - b}"
        elif operacion == '*':
            return f"Resultado: {a * b}"
        elif operacion == '/':
            if b != 0:
                return f"Resultado: {a / b}"
            else:
                return "No se puede dividir por cero."
        else:
            return "Operación no válida."
    except ValueError:
        return "Entrada inválida."

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Análisis de lista de números reales")
    print("2. Área y perímetro de un rectángulo")
    print("3. Verificar si un número es primo")
    print("4. Análisis de calificaciones")
    print("5. Estadísticas de lista de enteros")
    print("6. Calculadora básica")
    print("7. Salir")

# --- Bucle principal ---
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-7): ")

    match opcion:
        case "1":
            lista = pedir_lista_reales()
            print(f"Suma total: {suma_total(lista)}")
            print(f"Promedio: {promedio(lista):.2f}")
            pos, neg, ceros = contar_signos(lista)
            print(f"Positivos: {pos}, Negativos: {neg}, Ceros: {ceros}")
            print(f"Múltiplos de 3: {multiplos_de_tres(lista)}")
        case "2":
            try:
                base = float(input("Base del rectángulo: "))
                altura = float(input("Altura del rectángulo: "))
                print(f"Área: {area_rectangulo(base, altura)}")
                print(f"Perímetro: {perimetro_rectangulo(base, altura)}")
            except ValueError:
                print("Entrada inválida.")
        case "3":
            try:
                num = int(input("Ingrese un número entero: "))
                if es_primo(num):
                    print(f"{num} es primo.")
                else:
                    print(f"{num} no es primo.")
            except ValueError:
                print("Debe ingresar un número entero.")
        case "4":
            calis = pedir_calificaciones()
            if calis:
                prom, altas, riesgo = analizar_calificaciones(calis)
                print(f"Promedio: {prom:.2f}")
                print(f"Calificaciones altas (≥85): {altas}")
                print(f"En zona de riesgo (<60): {riesgo}")
        case "5":
            lista = pedir_lista_enteros()
            print(f"Mayor: {mayor(lista)}")
            print(f"Menor: {menor(lista)}")
            print("Frecuencia de elementos:")
            frec = frecuencia(lista)
            for num, rep in frec.items():
                print(f"{num}: {rep} veces")
        case "6":
            resultado = calculadora()
            print(resultado)
        case "7":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        case _:
            print("Opción inválida. Intente de nuevo.")
