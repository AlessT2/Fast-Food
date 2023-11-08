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