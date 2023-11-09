import queue
order_queue = queue.Queue()
vector_menus = []
vector_drinks = []
vector_order = []

class Customers:
    def __init__(self, name="", last_name="", nit="", e_mail="", phone_number="", age=0):
        self.name = name
        self.last_name = last_name
        self.nit = nit
        self.e_mail = e_mail
        self.phone_number = phone_number
        self.age = age

class Staff:
    def __init__(self, name="", last_name="", employee_code="", phone_number="", age=0):
        self.name = name
        self.last_name = last_name
        self.employee_code = employee_code
        self.phone_number = phone_number
        self.age = age

class Menus:
    def __init__(self, menu_name="", menu_description="", menu_price=""):
        self.menu_name = menu_name
        self.menu_description = menu_description
        self.menu_price = menu_price

    def menu_entry(self):
        print("Ingreso de Menús")
        self.menu_name = input("Ingrese el nombre del menú: ")
        self.menu_description = input("Ingrese una breve descripcion del menú: ")
        self.menu_price = int(input("Ingrese el precio del Menú: "))
        print("Menú registrado exitosamente")


class Drinks:
    def __init__(self, drink_name=0, drink_price=0):
        self.drink_name = drink_price
        self.drink_price = drink_price

    def drink_entry(self):
        print("Ingreso de bebidas")
        self.drink_name = input("Ingrese el nombre de la bebida: ")
        self.drink_price = int(input("ingrese el precio de la bebida: "))
        print("La bebida se registro exitosamente")

def mod_menu_name(menu_name):
    print("Modificar precio del Menú")
    #while not vector_menus.empty():
    for menu in vector_menus:
        if menu.menu_name == menu_name:
            menu.menu_price = int(input("Ingrese el nuevo precio del menú: "))
            return "El nuevo precio del menú es: ",menu.menu_name
    else:
        return "El nombre del menú ingresado aún no ha sido registrado"

def add_order_queue():
    print("Acciones de pedidos")
    print("1. Pedidos pendientes")
    print("2. Pedido en preparación")
    print("3. Marcar pedido más antiguo listo para servir")
    try:
        #first_order = order_queue.get()
        order_actions = int(input("Ingrese que acción desea realizar: "))
        if order_actions == 1:
            print("Los pedidos pendientes son: ",len(order_queue.queue))
        elif order_actions == 2:
            #preparing_order = order_queue.get()
            print("El pedido que se está preparando es: ",order_queue.get())
        elif order_actions == 3:
            print("El pedido que está listo para servir es: ",order_queue.get())

    except ValueError:
        print("Por favor ingrese una acción válida entre 1 y 3")

while True:
    print("Roles")
    print("1. Empleados")
    print("2. Clientes ")
    try:
        roles = int(input("Seleccione cual es su Rol: "))
        if roles == 1:
            print("Acciones de empleados")
            print("1. Agregar Menus")
            print("2. Agregar Bebidas")
            print("3. Modificar nombre del menus")
            print("4. Modificar precio del menu")
            print("5. Pedidos")

            try:
                employee_actions = int(input("Ingrese que acción desea realizar: "))
                menu = Menus()
                if employee_actions == 1:
                    menu.menu_entry()
                    vector_menus.append(menu)
                elif employee_actions == 2:
                    drink = Drinks()
                    vector_drinks.append(drink.drink_entry())
                    #drink.drink_entry()
                    #vector_drinks.append(drink)
                elif employee_actions == 3:
                    menus.mod_menu_name()
                else:
                    print("Por favor ingrese un valor válido de acciones para empleados")
            except ValueError:
                print("Por favor ingrese un valor válido de acciones para empleados")
        elif roles == 2:
            print("Acciones de clientes")
        else:
            print("Por favor ingrese un valor entero entre 1 y 5 para seleccionar su Rol")
    except ValueError:
        print("Por favor ingrese un valor entero entre 1 y 5 para seleccionar su Rol")