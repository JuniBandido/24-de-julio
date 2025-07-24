#Funciones
#en progra orientada a objetos se le dice metodos
def promedio():
    nums = []
    while True:
        action = input("1. Ingresar número\n2. Ya ingresé todos los numeros\n")
        match action:
            case "1":
                num = int(input("Ingresa el número: "))
                nums.append(num)
            case "2":
                break
    print(f"1. La suma de todos los numeros es de {sum(nums)}")
    print(f"2. El promedio es de {sum(nums)/len(nums)}")
    print(f"3. La cantidad de numeros positivos es de ")


