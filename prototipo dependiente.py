"""Complemento para el código de Lesther"""
"""Acciones para clientes"""
"Ordenar las posiciones y permitir recibir pedidos de los clientes"
while True:
    menu = input("*****Pedidos*****\nA. Registrar cliente"
    "\nB. Verificar su registro\nC. Cola de clientes\nD. \nE. \nElija su opción: ").lower()
    while menu == "a":
        # Agregar algunos clientes
        customers_queue.add_customer()
        break
    while menu == "b":
        # verificar cliente
        number = input("Ingrese el nit del cliente a verificar: ")
        customers_queue.verify_customer(number)  # Número o valor del nit a buscar
        break
    while menu == "c":
        # Mostrar la cola de clientes
        customers_queue.display_customers()
        break
    while menu == "d":
        break
    while menu == "e":
        break
    Continuar = input("\033[1;38;2;203;231;0m¿Desea continuar con el programa?\033[0;m\n"+"\033[1;38;2;162;233;29mS\033[0;m" + "/" + "\033[1;38;2;215;0;0mN \033[0;m").lower()
    if Continuar == "n":
            print("\033[1;38;2;231;0;95mPrograma Finalizado\033[0;m\n")
            break