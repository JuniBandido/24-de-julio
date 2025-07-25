products = []


while True:
    menu = input(
        "1. Agregar un producto a la lista\n2. Modificar un producto existente\n3. Eliminar un producto\n4. Ver todos los productos\n5. Salir del programa\n")

    match menu:
        case "1":
            new_product = input("Agregar producto a la lista: ")
            products.append(new_product)
            print("Producto agregado a la lista!")

        case "2":
            print("Tu lista actual es de: ",products)
            index = int(input("Ingrese el indice del que desea modificar: "))
            new_prodcut_name = input("Ingresa el nuevo valor: ")
            products[index] = new_prodcut_name
            print("Elemento modificado!")

        case "3":
            print("Tu lista actual es de: ",products)
            index = int(input("Ingrese el indice del que desea eliminar: "))
            products.remove(products[index])
            print("Producto eliminado!")

        case "4":
            print("Tu lista actual es de: ",products)

        case "5":
            print("bye bye :)")
            break

        case _:
            print("Opcion no dispopnible :(")