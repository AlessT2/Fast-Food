import queue

class Customer:
    def __init__(self):
        self.name = input("Nombre: ")
        self.last_name = input("Apellido: ")
        self.nit = input("NIT: ")
        self.phone_number = input("Teléfono: ")
        self.e_mail = input("Correo electrónico: ")

class CustomersQueue:
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

    def verify_customer(self, nit):
        for customer in self.customers.queue:
            if customer.nit == nit:
                print("El cliente está registrado.")
                # Aquí se puede permitir que el cliente realice un pedido
                return
        print("El cliente no está registrado. Por favor, regístrese.")
        # Aquí se puede solicitar al cliente que se registre

# Crear una nueva cola de clientes
customers_queue = CustomersQueue()

# Agregar algunos clientes
customers_queue.add_customer()

# verificar cliente
customers_queue.verify_customer("15")

# Mostrar la cola de clientes
customers_queue.display_customers()

#ofertas especiales///////////////////////////////////////////////////////////////////////
class DiscountManager:
    def __init__(self, discount=0):
        self.discount = discount

    def apply_discount(self, price):
        return price * (1 - self.discount)

#modificar la clase Buy para que funcionen los descuentos
class Buy:
    def __init__(self, cost, price, name, discount_manager=None):
        self.cost = cost
        self.price = price
        self.total = "\033[1;38;2;233;255;12m ¿Qué cantidad desea comprar? \033[0;m"
        self.name = name
        self.discount_manager = discount_manager

    def result(self):
        global WALLET
        print(f"\033[1;38;2;255;170;0m{self.name} \033[0m" + "\033[1;38;2;243;255;0mCuesta $\033[0;m", self.cost)
        t = int(input(self.total))
        if self.discount_manager:
            self.price = self.discount_manager.apply_discount(t * self.cost)
        else:
            self.price = t * self.cost
        if WALLET >= self.price:
            WALLET -= self.price
            print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
        else:
            print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")

#modificar la opción "e" del menú para que funcionen los descuentos
while product == "a":
    if __name__ == "__main__":
        discount_manager = DiscountManager(discount=DESCUENTO_GLOBAL)
        get_product1 = Product1("", "", "")
        get_product1.result(discount_manager=discount_manager)  # Pasar el descuento
    break

while product == "b":
    if __name__ == "__main__":
        discount_manager = DiscountManager(discount=DESCUENTO_GLOBAL)
        get_product2 = Product1("", "", "")
        get_product2.result2(discount_manager=discount_manager)  # Pasar el descuento
    break
