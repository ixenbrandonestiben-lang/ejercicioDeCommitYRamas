productos = []

def menu ():
        separador()
        print("     SISTEMA DE INVENTARIO        ")
        print("1. Agregar producto")
        print("2. listar productos")
        print("3. actualizar producto")
        print("4. eliminar producto")
        print("5. calcular valor total del inventario")
        print("6. salir")   
    
        
def agregar():
#agregar un producto nuevo a la lista de productos 
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: ")) 
    producto={
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    
     }
    productos.append(producto)
    
def listar():
    print("Lista de productos:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
        
        
def separador():
    print("-"*60)

def opc():
    while True:
        try:
            opc = int(input("Ingrese una opcion: "))
            return opc
        except ValueError as e:
            print(f"opcion no valida, tipo de error {e}.")

while True:
    menu()
    separador()
    op = opc()
    separador()
    if op == 1:
            agregar()
            
    elif op == 2:
        listar()
    elif op == 3:    
        print("Actualizar producto")
    elif op == 4:
        print("Eliminar producto")
    elif op == 5:
        print("Calcular valor total del inventario")
    elif op == 6:
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion no valida, intente de nuevo.")
    
        