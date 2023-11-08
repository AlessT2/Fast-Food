while True:
    print("///Escoja su tipo de pago///")
    menu = input("1. Efectivo."
                 "\n2. Tarjeta de crédito."
                 "\nSeleccione su opción: ")
    while menu == 1:
        print("Haz pagado", cantidad)
    while menu == 2:
        print("Se ha descontado ", cantidad, "de su cuenta.")
    continuar = input("¿Desea continuar en este menú?(S/N): ").upper()
    if continuar.lower() != "s":
        break