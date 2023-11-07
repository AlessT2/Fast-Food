vector_menus = []
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

    def data_entry(self):
        print("Ingreso de Menús")
        self.menu_name = input("Ingrese el nombre del menú: ")
        self.menu_description = input("Ingrese una breve descripcion del menú: ")
        self.menu_price = int(input("Ingrese el precio del Menú: "))

def mod_menu_name(name):
        print("Modificar nombre del Menú")
        #while not vector_menus.empty():
        for menu in vector_menus:
            if menu.menu_name == name:
                print("El menú entero es: ",menu)
                new_menu_name = input("Ingrese el nuevo nombre del menú: ")
                new_menu_name = menu.menu_name
                return print("El nuevo nombre del menú es: ",new_menu_name)
        #else:
        #    return print("NO se a ingresado ningún menu")

while True:
    print("Roles")
    print("1. Empleados")
    print("2. Clientes ")
    try:
        roles = int(input("Seleccione cual es su Rol: "))
        if roles == 1:
            print("Acciones de empleados")
            print("1. Agregar Menus")
            print("2. Modificar nombre del menus")
            print("3. Modificar precio del menu")
            try:
                employee_actions = int(input("Ingrese que acción desea realizar: "))
                if employee_actions == 1:
                    menu = Menus()
                    menu.data_entry()
                    vector_menus.append(menu)
                elif employee_actions == 2:
                    menu_name = input("Ingrese el nombre del menú que desea modificar: ")
                    print(mod_menu_name(menu_name))
                else:
                    print("Por favor ingrese un valor válido de acciones para empleados")
            except ValueError:
                print("Por favor ingrese un valor válido de acciones para empleados")
        elif roles == 2:
            print("Acciones de clientes")
        else:
            print("Por favor ingrese un valor entero entre 1 y 2 para seleccionar su Rol")
    except ValueError:
        print("Por favor ingrese un valor entero entre 1 y 2 para seleccionar su Rol")
