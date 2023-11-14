def crear_factura():
    information = []
    header = "Nombre; Apellido; NIT; Nombre de menú; Descripción del menú; Precio del menú\n"
    information.append(header)
    string = self.name + "; " + self.last_name + "; " + self.nit + "; " + self.menu_name + "; " + self.menu_description + "; " + self.menu_price + "\n"
    information.append(string)
    print("Datos almacenados correctamente")
    archive = open("Factura.csv", "w")
    archive.writelines(information)
    archive.close()

while True:
    print("///Escoja su tipo de pago///")
    print("1. Efectivo. \n2. Tarjeta de crédito.")
    try:
        menu = int(input("Seleccione su opción: "))
        while menu == 1:
            print("Haz pagado", cantidad)
            break
        while menu == 2:
            print("Se ha descontado ", cantidad, "de su cuenta.")
            break
        continuar = input("¿Desea continuar en este menú?(S/N): ").upper()
        if continuar.lower() != "s":
            break
    except ValueError:
        print("Seleccione una opción correcta.")