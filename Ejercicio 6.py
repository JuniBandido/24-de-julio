def promedio():
    nums = []
    negative_nums = 0
    positive_nums = 0
    while True:
        action = input("1. Ingresar número\n2. Ya ingresé todos los numeros\n")
        match action:
            case "1":
                num = int(input("Ingresa el número: "))
                nums.append(num)
                if num < 0:
                    negative_nums += 1
                elif num > 0:
                    positive_nums += 1
            case "2":
                break
            case _:
                print("Número no válido")
    print(f"1. La suma de todos los numeros es de {sum(nums)}")
    print(f"2. El promedio es de {sum(nums)/len(nums)}")
    print(f"3. La cantidad de numeros positivos es de {positive_nums} y la cantidad de números negativos es de {negative_nums} ")

def CalcularArea():
    b = int(input("Ingresa la base del triangulo: "))
    h = int(input("Ingresa la altura del triangulo: "))
    return b * h / 2

def ParOImpar():
    num = int(input("Ingresa un número: "))
    if num % 2 == 0:
        print(f"El número {num} es par")
    else:
        print(f"El número {num} es impar")

def PromedioCalificaciones():
    nums = []
    while True:
        action = input("1. Ingresar calificacion\n2. Calcular promedio\n")
        match action:
            case "1":
                num = int(input("Ingresa el número: "))
                nums.append(num)
            case "2":
                print(f"El promedio es de {sum(nums) / len(nums)}")
                break
            case _:
                print("Número no válido")

def mayorMenor():
    nums = []
    while True:
        action = input("1. Agregar número\n2. Mayor y Menor\n")
        if action == "1":
            num = int(input("Ingrese número: "))
            nums.append(num)
            print(nums)
        elif action == "2":
            mayor = max(nums)
            minimo = min(nums)
            print(f"El número {mayor} es el mayor")
            print(f"El número {minimo} es el menor")
            break
        else:
            print("Accion no válida")

while True:
    menu = input("Bienvenido al programa\n"
                 "Qué deseas realizar?\n"
                 "1. Ingresar n números y mostrar:\n La suma total,\n"
                 " El promedio,\n"
                 " La cantidad de números positivos y negativos\n"
                 "2. Calcular el área de un triángulo\n"
                 "3. Verificar si un número es par o impar\n"
                 "4. Calcular el promedio de n calificaciones\n"
                 "5. Ingresar n números y mostrar el mayor y el menor\n"
                 "6. Salir\n")
    match menu:
        case "1":
            promedio()
        case "2":
            area = CalcularArea()
            print(f"El area del triangulo es de {area}")
        case "3":
            ParOImpar()
        case "4":
            PromedioCalificaciones()
        case "5":
            mayorMenor()
        case "6":
            print("Hasta luego")
            exit()
        case _:
            print("Opcion no válida")