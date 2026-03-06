def menu ():
    try:
        separador()
        print("     SISTEMA DE INVENTARIO        ")
        print("1. Agregar producto")
        print("2. listar productos")
        print("3. actualizar producto")
        print("4. eliminar producto")
        print("5. calcular valor total del inventario")
        print("6. salir")
        separador()
        opc()
        separador()
    except ValueError:
        print("opcion no valida, porfavor ingrese un numero (1-6) .")
        

def separador():
    print("-"*60)

def opc():
    opc = int(input("Ingrese una opcion: "))
    return opc

while True:
    menu()
    try:
        if opc() == 1:
            print("Agregar producto")
        elif opc() == 2:
            print("Listar productos")
        elif opc() == 3:    
            print("Actualizar producto")
        elif opc() == 4:
            print("Eliminar producto")
        elif opc() == 5:
            print("Calcular valor total del inventario")
        elif opc() == 6:
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida, intente de nuevo.")
    except ValueError:
        print("opcion no valida, porfavor ingrese un numero (1-6) .")
        