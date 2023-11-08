# snake_case para variables, funciones y métodos
# PascalCase para clases
# SCREAMING_SNAKE_CASE para constantes
import random, time, queue, threading, datetime
"""*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"""
GET_BURGER = 0; GET_PIZZA = 0; GET_CHICKEN = 0; GET_SALAD = 0; GET_POTATO = 0; GET_FRICE = 0
GET_DONUTS = 0; GET_TACO = 0; GET_TEA = 0; GET_CHOCOLATE = 0; GET_COFEE = 0; GET_SHACKE = 0
GET_JUICE = 0; GET_WATER = 0; GET_SODA = 0; GET_CAPUCCINO = 0
"""*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"""
food_list = ["Hamburguesa","Pizza","Pollo","Ensalada","Papas fritas","Granizada","Rosquillas","Tacos"]
drink_list = ["Té","Chocolate","Café","Malteada","Jugo de frutas","Agua pura","Gaseosa","Capuchino"]
name_list_M = ["Juan","Carlos","Marcos","Andrés","Esteban","Noah","Dylan","Daniel","Nicolás", "Adrían"]
name_list_W = ["Kenya","Jessica","Issabela","Luna","Elena","Cassidy","Emily","Ruby","Vanessa","Abby"]
surnames_list = ["Sinclair","Merritt","Archer","Sterling","Wren","Hawthorne","Delaney","Whitaker","Kensington","Montgomery"]
payment_list = ["Efectivo","Tarjeta"]; fast = ["Hamburguesa","Pizza","Papas fritas"]
preferences_list = ["Comida saludable","Comida rápida","Ninguna preferencia"]
names_list = ["Hombre","Mujer"]; healthy = ["Pollo","Ensalada","Granizada"]
aleatory_preferences = random.choice(preferences_list)  # Elige una preferencia aleatoria
aleatory_name = random.choice(names_list)  # Elije un nombre aleatorio
"""*-*-*-*Condiciones*-*-*-*"""
def condition_name(w, m):
    if aleatory_name == "Hombre":
        return random.choice(m)
    if aleatory_name == "Mujer":
        return random.choice(w)
def condition_drink(b):
    return random.choice(b)
def condition_post_name(p):
    return random.choice(p)
def preference_preference(r):
    return random.choice(r)
def condition_preference(h,a,d):
    if aleatory_preferences == "Comida saludable":
        return random.choice(h)
    if aleatory_preferences == "Comida rápida":
        return random.choice(a)
    if aleatory_preferences == "Ninguna preferencia":
        return random.choice(d)
def condition_payment(e):
    return random.choice(e)
"""*-*-*Colas*-*-*"""
start_queue = queue.Queue()
date_queue = queue.Queue()
"""*-*-*Ingreso de los clientes y pedir que los atiendan*-*-*"""
def enter_customers():
    n = 1
    c = 1
    aleatory_time = random.uniform(5,15)
    while True:
        #print("\nHa ingresado un cliente a la tienda")
        time.sleep(2)
        c += 1
        #print("\nEl cliente ingresó a la cola y desea ser atendido")
        start_queue.put(n)
        n += 1
        time.sleep(aleatory_time)
"""*-*-*-*-*Ver clientes en la cola*-*-*-*-*-*"""
def see():
    while start_queue.empty():
        print("No hay clientes en la cola")
        break
    else:
        print("Hay clientes esperando en la cola")
"""*-*-*-*Atender a los clientes*-*-*-*"""
def attend_customers():
    while start_queue.empty():
        print("No hay clientes en la cola")
        break
    else:
        customer_number = start_queue.get()
        print(f"Atendiendo al cliente {customer_number}")
        element = [condition_name(name_list_W,name_list_M), condition_post_name(surnames_list),
        preference_preference(preferences_list),condition_preference(healthy,fast,food_list),
        condition_drink(drink_list),condition_payment(payment_list)]
        print(f"Sus datos son:",element)
        date_queue.put(element)
"""*-*-*-*-*-*-*Ver las ordenes y los nombres de los dueños*-*-*-*-*-*-*"""
def see_order():
    while date_queue.empty():
        print("No hay ordenes pendientes en la cola")
        break
    else:
        print(date_queue.queue)
"""*-*-*-*-*-*-*Ver el menú y poder cambiarle los precios*-*-*-*-*-*-*"""
cost1 = ["Hamburguesa $", 6]; cost2 = ["Pollo $", 5]; cost3 = ["Ensalada $", 4]
cost4 = ["Papas fritas $", 3]; cost5 = ["Granizada $", 6]; cost6 = ["Rosquillas $", 3]
cost7 = ["Tacos $", 5]; cost8 = ["Té $", 2]; cost9 = ["Chocolate $", 6]; cost10 = ["Café $", 4]
cost11 = ["Malteada $", 6]; cost12 = ["Jugo de frutas $", 3]; cost13 = ["Agua pura $", 1]
cost14 = ["Gaseosa $", 3]; cost15 = ["Capuchino $", 8]; cost16 = ["Pizza $", 5]
global c1
c1 = cost1[1]
c2 = cost16[1]
def show_menu():
    print(f"*-*-*-*Menú Princial*-*-*-*\n{cost1}{cost2}{cost3}{cost4}{cost5}\n{cost6}"
          f"{cost7}{cost8}{cost9}{cost10}\n{cost11}{cost12}{cost13}{cost14}{cost15}{cost16}")
    change = input("Ingrese el nombre de la comida para cambiarle el precio (Precione N/n para cancelar: )").lower()
    if change == "n":
        print("")
    if change == "hamburguesa":
        price = int(input(f"Ingrese el nuevo precio para la hamgurguesa: "))
        cost1[1] = price
    if change == "pizza":
        price = int(input(f"Ingrese el nuevo precio para la pizza: "))
        cost16[1] = price
    if change == "pollo":
        price1 = int(input(f"Ingrese el nuevo precio para el pollo: "))
        cost2[1] = price1
    if change == "ensalada":
        price2 = int(input(f"Ingrese el nuevo precio para la ensalada: "))
        cost3[1] = price2
    if change == "papas fritas":
        price3 = int(input(f"Ingrese el nuevo precio para las papas fritas: "))
        cost4[1] = price3
    if change == "granizada":
        price4 = int(input(f"Ingrese el nuevo precio para la granizada: "))
        cost5[1] = price4
    if change == "rosquilla":
        price5 = int(input(f"Ingrese el nuevo precio para la rosquilla: "))
        cost6[1] = price5
    if change == "taco":
        price6 = int(input(f"Ingrese el nuevo precio para el taco: "))
        cost7[1] = price6
    if change == "te":
        price7 = int(input(f"Ingrese el nuevo precio para el te: "))
        cost8[1] = price7
    if change == "chocolate":
        price8 = int(input(f"Ingrese el nuevo precio para el chocolate: "))
        cost9[1] = price8
    if change == "cafe":
        price9 = int(input(f"Ingrese el nuevo precio para el café: "))
        cost10[1] = price9
    if change == "malteada":
        price10 = int(input(f"Ingrese el nuevo precio para la malteada: "))
        cost11[1] = price10
    if change == "jugo de frutas":
        price11 = int(input(f"Ingrese el nuevo precio para el jugo de frutas: "))
        cost12[1] = price11
    if change == "agua pura":
        price12 = int(input(f"Ingrese el nuevo precio para el agua pura: "))
        cost13[1] = price12
    if change == "gaseosa":
        price13 = int(input(f"Ingrese el nuevo precio para la gaseosa: "))
        cost14[1] = price13
    if change == "capuchino":
        price14 = int(input(f"Ingrese el nuevo precio para el capuchino: "))
        cost15[1] = price14
    print(f"*-*-*-*Menú Princial*-*-*-*\n{cost1}{cost2}{cost3}{cost4}{cost5}\n{cost6}"
          f"{cost7}{cost8}{cost9}{cost10}\n{cost11}{cost12}{cost13}{cost14}{cost15}{cost16}")
"""*-*-*-*-*-*-*Actualizar la cantidad de comida con el sistema*-*-*-*-*-*-*"""
burgers = ["Hamburguesas", 0]; chicken = ["Pollo", 0]; salad = ["Ensalada", 0]; potato = ["Papas fritas", 0]
hailstorm = ["Granizada", 0]; Donuts = ["Rosquillas", 0]; tacos = ["Tacos", 0]; tea = ["Té", 0]
chocolate = ["Chocolate", 0]; cofee = ["Café", 0]; milk_shake = ["Malteada", 0]; juice = ["Jugo de frutas", 0]
water = ["Agua pura", 0]; soda = ["Gaseosa", 0]; cappuccino = ["Capuchino", 0]; pizza = ["Pizza", 0]
"""*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"""
STORE = [burgers, chicken, salad, potato, hailstorm, Donuts, tea, tea, chocolate, cofee, milk_shake, juice,water,soda, cappuccino]
"""*-*-*-*Comprar producto*-*-*-*"""
class Coin:
    def __init__(self, coin=50):
        self.coin = coin
    def show(self):
        return self.coin
BASE_COIN = Coin()
WALLET = BASE_COIN.show()
class Buy:
    def __init__(self, cost, price, name):
        self.cost = cost
        self.price = price
        self.total = "\033[1;38;2;233;255;12m                  ¿Qué cantidad desea comprar? \033[0;m"
        self.name = name

    def result(self):
        while True:
            global WALLET
            print(f"\033[1;38;2;255;170;0m{self.name} \033[0m" + "\033[1;38;2;243;255;0mCuesta $\033[0;m", self.cost)
            global f
            t = int(input(self.total))
            f = t
            self.price = t * self.cost
            0
            if WALLET >= self.price:
                WALLET -= self.price
                print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
                break
            print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
            break
class Product1(Buy):
    def __init__(self, cost, price, name):
        Buy.__init__(self, cost, price, name)
    def result(self):
        global GET_BURGER
        self.name = "Hamburguesa"
        self.cost = c1
        Buy.result(self)
        GET_BURGER += f
        burgers[1] = GET_BURGER
    def result2(self):
        global GET_PIZZA
        self.name = "Pizza"
        self.cost = c2
        Buy.result(self)
        GET_PIZZA += f
        pizza[1] = GET_PIZZA
"""*-*-*-*-*-*Tiempo*-*-*-*-*-*"""
mesaje = threading.Thread(target=enter_customers)
mesaje.daemon = True
mesaje.start()
while True:
    menu = input("\nA. Atender a los clientes\nB. Ver pedidos\nC. Ver el catálogo del menú\nD. Clientes en la cola\nE. Comprar productos\nF. Ver la cantidad de productos diponibles\nS. Acceder al sistema\nElija su opción: ").lower()
    while menu == "a":
        attend_customers()
        break
    while menu == "b":
        see_order()
        break
    while menu == "c":
        show_menu()
        break
    while menu == "d":
        see()
        break
    while menu == "s":
        #No disponible aún
        break
    while menu == "f":
        print(STORE)
        break
    while menu == "e":
        while True:
            print("\033[1;38;2;23;252;248mActualmente tienes:\033[0m", WALLET, "Monedas")
            product = input("\033[1;38;2;255;54;0m                                                  Productos \033[1;38;2;255;165;00m" + "disponibles:\033[0m\n"
            "\033[1;38;2;216;98;55mA. Hamburguesa  \033[0m" + "\033[1;38;2;51;214;243mB. Pizza     \033[0;m" + "\033[1;38;2;209;0;255mC. Pollo    \033[0;m" + "\033[1;38;2;244;155;0mD. Ensalada    \033[0m"
            "\033[1;38;2;255;224;0mE. Papas Fritas     \033[0;m" + "\033[1;38;2;255;6;210mF. Granizada\033[0;m\n" + "\033[1;38;2;180;255;71m           G. Rosquilla    \033[0;m" + "\033[1;38;2;255;185;71mH. Taco   \033[0;m"
            "\033[1;38;2;255;6;93mI. Té  \033[0;m" + "\033[1;38;2;25;238;187mJ. Chocolate   \033[0;m" + "\033[1;38;2;153;6;255mK. Café\033[0;m\n"
            "\033[1;38;2;6;157;255m                                                L. Malteada    \033[0;m" + "\033[1;38;2;78;255;6mM. Jugo de fruta     \033[0;m" + "\033[1;38;2;6;255;217mN. Agua pura\033[0;m\n"
            "\033[1;38;2;215;0;0m                                 O. Gaseosa\033[0;m\n" + "    P. Capuchino\033[0;m\n" + "\033[1;38;2;50;205;50m            Elija su opción: \033[0;m").lower()
            while product == "a":
                if __name__ == "__main__":
                    get_product1 = Product1("", "", "")
                    get_product1.result()
                break
            while product == "b":
                if __name__ == "__main__":
                    get_product2 = Product1("", "", "")
                    get_product2.result2()
                break
            break
        break
    Continuar = input("\033[1;38;2;203;231;0m¿Desea continuar con el programa?\033[0;m\n" + "\033[1;38;2;162;233;29mS\033[0;m" + "/" + "\033[1;38;2;215;0;0mN \033[0;m")
    if Continuar == "n" or Continuar == "N":
        print("\033[1;38;2;231;0;95mPrograma Finalizado\033[0;m\n")
        break