""" Administrar Clientes """
import enum
import re
import helpers

clientes= []

agustin= {'nombre': 'Agustin', 'apellido': 'Lobo', 'dni':'42643710'}
clientes.append(agustin)

clientes.append({'nombre': 'Tomas', 'apellido': 'Lobo', 'dni': '48365214'})
clientes.append({'nombre': 'Micaela', 'apellido': 'Lobo', 'dni': '50321478'})

#Funcion para mostrar un cliente
def show(client):
    print(f"{client['dni']}: {client['nombre']} {client['apellido']}")
    return "nombre"+client['nombre']+"apellido"+client['apellido']+"dni"+client['dni']

#Funicion para mostrar todos los clientes
def show_all():
    for client in clientes:
        show(client)

#Funcion para buscar clientes
def find():

    dni = input("Ingrese el dni del cliente que desea buscar:\n>")

    for i, client in enumerate(clientes):
        if client['dni'] == dni:
            show(client)
            return i, client
    
    print("No se a encontrado ningun cliente con el dni solicitado.")

#Funcion para validar el dni
def is_valid(dni):
    """
    >>> is_valid('42643710')
    False

    >>> is_valid('48365214')
    False

    >>> is_valid('123')
    False

    >>> is_valid('12345678')
    True

    """

    #comprueba si el dni cumple el patron
    if not re.match('[0-9]{7}',dni):
        return False

    #Ahora comprueba que no se repita
    for cliente in clientes:
        if cliente["dni"] == dni:
            return False
        
    return True

#Funcion para añadir un nuevo cliente
def agreagar():
    client = dict()
    
    print("Introduzca el nombre del cliente (Debe llevar de 2 a 30 caracteres)")
    client['nombre'] = helpers.input_text(2,30)

    print("Introduzca el apellido del cliente (Debe llevar de 2 a 30 caracteres)")
    client['apellido'] = helpers.input_text(2,30)

    while True:
        print("Introduzca el DNI del cliente (Este debecontar con 8 caracteres justos)")
        dni = helpers.input_text(8,8)
        if is_valid(dni)==True:
            client['dni'] = dni
            break
        print("ERROR.. El dni ingresado es incorrecto intente nuevamente...")
    
    clientes.append(client)
    return client


def edit():

    i, cliente = find()

    if cliente:
        
        print("\nModificando al cliente:")
        show(cliente)

        print("\nIngrese el nombre (Debe tener entre 2 y 30 caracteres): ")
        clientes[i]['nombre'] = helpers.input_text(2, 30)

        print("Ingrese el apellido (Debe tener entre 2 y 30 caracteres): ")
        clientes[i]['apellido'] = helpers.input_text(2, 30)

        return True
    return False

def delete():

    i, cliente = find()
        
    if cliente:
        cliente = clientes.pop(i)
        show(cliente)
        print("\n")
        return True
    print("\nERROR.. no se encontro ningun cliente con el dni: "+dni+"\n")
    return False

if __name__=="__main__":
    import doctest
    doctest.testmod()