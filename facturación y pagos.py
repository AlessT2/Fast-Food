def crear_factura(datos, encabezado, cadena):
    datos = []
    encabezado = "datos\n"
    datos.append(encabezado)
    cadena = "nombre" + "; " + "apellido" + "; " + "numero pedido" + "; " + "comida" + "\n"
    datos.append(cadena)
    print("Datos almacenados correctamente")
    archivo = open("Series favoritas.pdf", "w")
    archivo.writelines(datos)
    archivo.close()

while True:
    print("///Escoja su tipo de pago///")
    print("1. Efectivo. \n2. Tarjeta de crédito.")
    try:
        menu = int(input("Seleccione su opción: "))
        while menu == 1:
            print("Haz pagado", "cantidad")
            break
        while menu == 2:
            print("Se ha descontado ", "cantidad", "de su cuenta.")
            break
        continuar = input("¿Desea continuar en este menú?(S/N): ").upper()
        if continuar.lower() != "s":
            break
    except ValueError:
        print("Seleccione una opción correcta.")