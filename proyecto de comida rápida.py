import queue
vector_menus = []
vector_menu_price = []
vector_menus_description = []
vector_drinks = []
vector_drinks_price = []
order_queue = queue.Queue()
money = 0
obtained = 0
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
        vector_menus.append(self.menu_name)
        vector_menus_description.append(self.menu_description)
        vector_menu_price.append(self.menu_price)
        print("Menú registrado exitosamente")

    def mod_menu_price(self, menu, price):
        self.menu_name = menu
        print(f"El nuevo precio de {self.menu_name} es {price}")
class Drinks:
    def __init__(self, drink_name="", drink_price=""):
        self.drink_name = drink_name
        self.drink_price = drink_price

    def drink_entry(self):
        print("Ingreso de bebidas")
        self.drink_name = input("Ingrese el nombre de la bebida: ")
        self.drink_price = int(input("ingrese el precio de la bebida: "))
        vector_drinks.append(self.drink_name)
        vector_drinks_price.append(self.drink_price)
        print("La bebida se registro exitosamente")
def apply_discount(price):
    global obtained, money
    discount = 0.1  # Descuento del 10%
    discounted_price = price * (1 - discount)
    obtained += discounted_price
    money += obtained
    return discounted_price
def mod_menu_price():
    print("Modificar precio del Menú")
    if not len(vector_menus) == 0:
        print(vector_menus)
        search = input("Ingrese el nombre del menú al que le quiere cambiar el nombre: ")
        for i in range(len(vector_menus)):
            while vector_menus[i] == search:
                menu = Menus()
                print("El precio actual de ", vector_menus[i], "es: ", vector_menu_price[i])
                new = int(input("Ingrese el nuevo precio del menú: "))
                menu.mod_menu_price(vector_menus[i], new)
                vector_menu_price[i] = new
                break
        else:
            print("El menú con el nombre ingresado aún no ha sido registrado")
    else:
        return "Aún no se han registrado menús"

def add_order_queue():
    pendient = "\U0001F570"
    proces = "\U0001F504"
    print(f"\033[1;38;2;255;193;0m▼▲▼▲▼ Acciones de Pedidos {order} ▼▲▼▲▼\033[0;m \n")
    print("1. Pedidos pendientes")
    print("2. Pedido en preparación")
    print("3. Marcar pedido más antiguo listo para servir")
    try:
        order_actions = int(input("Ingrese que acción desea realizar: "))
        if order_actions == 1:
            print(f"\033[1;38;2;255;193;0m▼▲▼▲▼ Pedidos pendientes {pendient}: \033[0;m \n",len(order_queue.queue))
        elif order_actions == 2:
            while not order_queue.empty():
                print(f"\033[1;38;2;255;193;0m▼▲▼▲▼ El pedido que se está preparando es {proces}: \033[0;m \n",order_queue.queue[0])
                break
            print("No hay pedidos preparándose")
        elif order_actions == 3:
            while not order_queue.empty():
                print(f"\033[1;38;2;255;193;0m▼▲▼▲▼ El pedido que está listo apra servir es {yes}: \033[0;m \n",order_queue.get())
                crear_factura(total)
                break
            print("No hay pedidos listos")

    except ValueError:
        print("Por favor ingrese una acción válida entre 1 y 3")
def search_menu(list_, element):
    for i in range(len(list_)):
        if list_[i] == element:
            return 1
    return -1
def search_menu2(list_, element):
    for i in range(len(list_)):
        if list_[i] == element:
            return i
    return -1
def food_pay(list_, element):
    for i in range(len(list_)):
        if i == element:
            return list_[i]
    return -1
def drink_pay(list_, element):
    for i in range(len(list_)):
        if i == element:
            return list_[i]
def get_queue():
    while True:
        print("***Solicitar el pedido***")
        print(f"El menú de comida es el siguiente: {vector_menus}{vector_menus_description}{vector_menu_price}")
        food = input("Escriba el nombre de la comida a elegir: ")
        s = search_menu(vector_menus, food)
        if s == 1:
            print(f"El menú de bebida es el siguiente: {vector_drinks}{vector_drinks_price}")
            food_drik = input("Escriba el nombre de la bebida a elegir: ")
            d = search_menu(vector_drinks, food_drik)
            if d == 1:
                print("Pedido ingresado a la cola de Pedidos")
                order_queue.put(food, food_drik)
                s2 = search_menu2(vector_menus, food)
                d2 = search_menu2(vector_drinks, food)
                pay1 = food_pay(vector_menu_price,s2)
                pay2 = drink_pay(vector_drinks_price, d2+1)
                global total
                total = pay1 + pay2
                print(f"Total a pagar {pay1} + {pay2} = {total}")
                break
            print("No se encuentra esa bebida, intente otra vez")
        print("No se encuentra esa comida, intente otra vez")
class Customer:
    def __init__(self):
        self.name = input("Nombre: ")
        self.last_name = input("Apellido: ")
        self.nit = input("NIT: ")
        self.phone_number = input("Teléfono: ")
        self.e_mail = input("Correo electrónico: ")

def crear_factura(cantid):
    information = []
    header = "Nombre; Apellido; NIT; Nombre de menú; Descripción del menú; Precio del menú\n"
    information.append(header)
    customer = Customer()
    menus = Menus()
    print(customer.name, customer.last_name, customer.nit, menus.menu_name, menus.menu_description, menus.menu_price)
    string = customer.name + "; " + customer.last_name + "; " + customer.nit + "; " +  menus.menu_name + "; " + menus.menu_description + "; " + menus.menu_price + "\n"
    information.append(string)
    print("Datos almacenados correctamente")
    archive = open("Factura.csv", "w")
    archive.writelines(information)
    archive.close()
    print("///Escoja su tipo de pago///")
    print("1. Efectivo. \n2. Tarjeta de crédito.")
    while True:
        cantidad = cantid
        try:
            opcion = int(input("Seleccione su opción: "))
            while opcion == 1:
                print("Has pagado", cantidad)
                print(f"Pero como oferta, ahora se descuenta el 10% a su pago: {apply_discount(cantidad)}")

                break
            while opcion == 2:
                print("Se ha descontado ", cantidad, "de su cuenta.")
                print(f"Per como oferta, ahora se descuenta el 10% a su pago: {apply_discount(cantidad)}")
                break
            continuar = input("¿Desea continuar en este menú?(S/N): ").upper()
            if continuar.lower() != "s":
                break
        except ValueError:
            print("Seleccione una opción correcta.")
        break
class CustomersQueue(Menus):
    def __init__(self):
        self.customers = queue.Queue()
    def add_customer(self):
        customer = Customer()
        self.customers.put(customer)
    def display_customers(self):
        while not self.customers.empty():
            customer = self.customers.get()
            print("Nombre:", customer.name)
            print("Apellido:", customer.last_name)
            print("NIT:", customer.nit)
            print("Teléfono:", customer.phone_number)
            print("Correo electrónico:", customer.e_mail)
            print("")
        else:
            print("No hay clientes en la cola")
    def verify_customer(self, nit):
        for customer in self.customers.queue:
            if customer.nit == nit:
                print("El cliente está registrado...")
                if len(vector_menus) != 0 and len(vector_drinks) != 0:
                    get_queue()
                    break
                print("No hay comida o bebida registrado en el sistema")
        print("El cliente no está registrado. Por favor, ingrese a la opción A y luego regrese.")
customers_queue = CustomersQueue()
while True:
    shop = "\U0001F3EA"
    employee = "\U0001F468\U0000200D\U0001F4BC"
    chef = "\U0001F468\U0000200D\U0001F373"
    choose = "\U0001F914"
    hamburger = "\U0001F354"
    potato_chips = "\U0001F35F"
    billet= "\U0001F4B5"
    soda = "\U0001F964"
    order = "\U0001F4DC"
    computer = "\U0001F4BB"
    print(f"\033[1;38;2;255;143;0m/\/\/\ Roles {shop} /\/\/\ \033[0;m")
    print(f"\033[1;38;2;243;82;7m○○○○○ 1. Empleados {chef} ○○○○ \033[0;m")
    print(f"\033[1;38;2;3;173;0m▬▬▬▬▬ 2. Clientes {employee} ▬▬▬▬▬ \033[0;m")
    print(f"\033[1;38;2;0;147;255m▲▼▲▼▲▼  3. Sistema {computer} ▲▼▲▼▲▼  \033[0;m")
    try:
        roles = int(input(f"\033[1;38;2;229;240;0m {choose} Seleccione cual es su Rol: \033[0;m\n"))
        if roles == 1:
            print(f"\033[1;38;2;243;82;7m▲▼▲▼▲▼ Acciones de empleados {chef} ▲▼▲▼▲▼ \033[0;m")
            print(f"\033[1;38;2;240;197;0m///// 1. Agregar menús {hamburger}{potato_chips} ///// \033[0;m")
            print(f"\033[1;38;2;0;171;240m ▼▬▼▬▼ 2. Agregar bebidas {soda} ▼▬▼▬▼ \033[0;m")
            print(f"\033[1;38;2;0;240;171m▼$▼$▼ 3. Modificar precio del menu {billet}{hamburger}{potato_chips}{billet} ▼$▼$▼ \033[0;m")
            print(f"\033[1;38;2;255;193;0m▼-▼-▼ 4. Pedidos {order} ▼-▼-▼ \033[0;m")
            try:
                employee_actions = int(input(f"\033[1;38;2;229;240;0m {choose} Ingrese que acción desea realizar: \033[0;m\n"))
                if employee_actions == 1:
                    menu = Menus()
                    menu.menu_entry()
                elif employee_actions == 2:
                    drink = Drinks()
                    vector_drinks.append(drink.drink_entry())
                elif employee_actions == 3:
                    mod_menu_price()
                elif employee_actions == 4:
                    add_order_queue()
                else:
                    print("Por favor ingrese un valor válido de acciones para empleados")
            except ValueError:
                print("Por favor ingrese un valor válido de acciones para empleados")
        elif roles == 2:
            register = "\U0001F4DA"
            yes = "\U00002705"
            queue_custom = "\U0001F6B6\U0000200D\U00002642\U0000FE0F"
            print(f"\033[1;38;2;3;173;0m○○○○○ Acciones de clientes {employee} ○○○○○ \033[0;m")
            menu = input(f"\033[1;38;2;255;193;0m                   ▲-▲-▲ Pedidos {order} ▲-▲-▲ \033[0;m\n"+
            f"\033[1;38;2;255;131;0m             ▲-▲-▲ A. Registrar cliente {register} ▲-▲-▲ \033[0;m\n"
            f"\033[1;38;2;255;240;0m            ▲=▲=▲ B. Verificar su registro {yes} ▲=▲=▲ \033[0;m\n"
            f"\033[1;38;2;243;8;236m            ▲▬▲▬▲ C. Cola de clientes {queue_custom}{queue_custom}{queue_custom} ▲▬▲▬▲ \033[0;m\n"
            f"\033[1;38;2;229;240;0m{choose} Elija su opción: \033[0;m\n").lower()
            while menu == "a":
                customers_queue.add_customer()
                break
            while menu == "b":
                number = input("Ingrese el nit del cliente a verificar: ")
                customers_queue.verify_customer(number)  # Número o valor del nit a buscar
                break
            while menu == "c":
                customers_queue.display_customers()
                break
            Continuar = input("\033[1;38;2;203;231;0m¿Desea continuar con el programa?\033[0;m\n" + "\033[1;38;2;162;233;29mS\033[0;m" + "/" + "\033[1;38;2;215;0;0mN \033[0;m").lower()
            if Continuar == "n":
                print("\033[1;38;2;231;0;95mPrograma Finalizado\033[0;m\n")
                break
        elif roles == 3:
            print(f"\033[1;38;2;0;147;255m▲▼▲▼▲▼  3. Sistema {computer} ▲▼▲▼▲▼  \033[0;m")
            print(f"Menús disponibles: {vector_menus}{vector_menus_description}{vector_menu_price}")
            print(f"Bebidas disponibles: {vector_drinks}{vector_drinks_price}")
            print(f"Dinero actual: {money}")
            print(f"Dinero obtenido: {obtained}")
        else:
            print("Por favor ingrese un valor entero entre 1 y 2 para seleccionar su Rol")
    except ValueError:
        print("Por favor ingrese un valor entero entre 1 y 2 para seleccionar su Rol")