from clientes import Cliente
from equipos import Equipo

clientes = []

def buscar_cliente(nombre):
    for c in clientes:
        if nombre in c.get_nombre_completo():
            return c
        
def menu():
    while True:
        print("1. Ingresar cliente: ")
        print("2. Ver ciente: ")
        print("3. Agregar Equipos: ")
        print("4. Ver equipos por cliente: ")
        opcion = input("Elija una opcion: ")

        if opcion == "1":
             nombre = input("Nombre: ")
             apellidos = input("Apellidos:")
             telefono = input("Telefono: ")
             clientes = Cliente(nombre, apellidos, telefono)
             clientes.append(Cliente)
             print("Cliente registrado.")

        elif opcion == "2":
            for c in clientes:
                print(c)

        elif opcion == "3":
            nombre = input("Nombre del cliente: ")
            Cliente = buscar_cliente(nombre)
            if Cliente:
                numero = input("Numero de parte: ")
                tipo = input("Tipo de equipo: ")
                Equipo = Equipo(numero, tipo)
                Cliente.agregar_equipo(Equipo)
                print("Equipo Agregadpo.")
            else:
                print("Cliente no encontrado.")

        elif opcion == '4':
            nombre = input("Nombre del cliente: ")
            cliente = buscar_cliente(nombre)
            if cliente:
                if cliente.equipos:
                    for e in cliente.equipos:
                        print(e)
                else:
                    print("El cliente no tiene equipos registrados.")
            else:
                print("Cliente no encontrado.")
       # taller-de-reparacion-de-equipos-de-computo /c/Users/umg.LABHUE/Desktop/tarea/clientes.py /c/Users/umg.LABHUE/Desktop/tarea/equipos.py
