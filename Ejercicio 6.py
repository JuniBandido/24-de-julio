#Funciones
#en progra orientada a objetos se le dice metodos
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



