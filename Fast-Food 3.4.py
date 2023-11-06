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


while True:
    print("Roles")
    print("1. Empleados")
    print("2. Clientes ")
    try:
        roles = int(input("Seleccione cual es su Rol: "))
        if roles == 1:
            print("Acciones de empleados")
        elif roles == 2:
            print("Acciones de clientes")
        else:
            print("Por favor ingrese un valor entero entre 1 y 2 para seleccionar su Rol")
    except ValueError:
        print("Por favor ingrese un valor entero entre 1 y 2 para seleccionar su Rol")
