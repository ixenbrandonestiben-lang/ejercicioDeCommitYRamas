productos = [
    {
        "nombre": "mazana",
        "cantidad": 10,
        "precio": 5
    },
    {
        "nombre": "banana",
        "cantidad": 20,
        "precio": 3
    },
    {
        "nombre": "naranja",
        "cantidad": 15,
        "precio": 5
    },
    {
        "nombre": "pera",
        "cantidad": 12,
        "precio": 6
    }
]

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
    try:
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: ")) 
        producto={
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        
        }
        productos.append(producto)
    except ValueError:
        print("Error: cantidad y precio deben ser numeros.")
        
        
def listar():
    print("Lista de productos:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
        
def actualizar():
    try:
        nombre = input("Ingrese el nombre del producto a actualizar: ")
        cantidad = int(input("Ingrese la nueva cantidad del producto: "))
    
        encontrado = False
    
        for producto in productos:
            if producto["nombre"] == nombre:
                producto["cantidad"] = cantidad
                print(f"Cantidad del producto '{nombre}' actualizada a {cantidad}.")
                break
            else:
                print(f"Producto '{nombre}' no encontrado en el inventario.")
    except ValueError:
        print("Error: cantidad debe ser un numero entero.")
        
def eliminar():
    try:
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        encontrado = False
    
        for producto in productos:
            if producto["nombre"] == nombre:
                productos.remove(producto)
                print(f"Producto '{nombre}' eliminado del inventario.")
                encontrado = True
                break
        
        if not encontrado:
            print(f"Producto '{nombre}' no encontrado en el inventario.")
    except ValueError:
        print("Error: cantidad debe ser un numero entero.")

def valorInventario():
    try:
        total = 0
        for producto in productos:
            total += producto["precio"] * producto["cantidad"]
        print(f"El valor total del inventario es: {total}")
    except ValueError:
        print("Error: cantidad y precio deben ser numeros.")
   
              
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
        actualizar()
    elif op == 4:
        eliminar()
    elif op == 5:
        valorInventario()
    elif op == 6:
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion no valida, intente de nuevo.")
    
        