"""Estos códigos a continuación son complementos de los códigos del inciso 3 hasta el 6"""
"Se añadió a las listas el nombre, descripción y precio para cada menú:"
vector_menus.append(self.menu_name)
vector_menu_description.append(self.menu_description)
vector_menu_price.append(self.menu_price)
"Se añadieron 4 funciones que permiten encontrar y mostrar cada menú para que el cliente" \
"pueda escoger libremente; esto es cuando se le está atendiendo al cliente"
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
                pay2 = drink_pay(vector_drinks_price, d2)
                global total
                total = pay1 + pay2
                print(f"Total a pagar {total}")
                break
            print("No se encuentra esa bebida, intente otra vez")
        print("No se encuentra esa comida, intente otra vez")