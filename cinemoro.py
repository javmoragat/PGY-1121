cantv = 0
valenni = 0
valenjo = 0
valenad = 0
ventni = 0
ventjo = 0
ventad = 0
cantvni = 0
cantvjo = 0
cantvad = 0
canttni = 0
canttjo = 0
canttad = 0
ventt = 0
cantdvv = 0

while True:
    print("====================================")
    print("     Categorias de Entradas         ")
    print("Niño: $5.500 Edad (1-13)            ")
    print("Joven: $7.000 Edad (14-21)          ")
    print("Adulto: $9.000 Edad (22 En adelante)")
    print("====================================")
    categ = input("Ingrese categoría de entrada: ")

    if categ.lower() == "niño":
        cantvni = int(input("Ingrese cantidad de entradas: "))
        valenni = cantvni * 5500
        print("El valor total es: $", valenni)
        ventni += valenni
        canttni += cantvni
        print("Gracias por su compra, disfrute la función")
    
    elif categ.lower() == "joven":
        cantvjo = int(input("Ingrese cantidad de entradas: "))
        valenjo = cantvjo * 7000
        print("El valor total es: $", valenjo)
        ventjo += valenjo
        canttjo += cantvjo
        print("Gracias por su compra, disfrute la función")

    elif categ.lower() == "adulto":
        cantvad = int(input("Ingrese cantidad de entradas: "))
        valenad = cantvad * 9000
        print("El valor total es: $", valenad)
        ventad += valenad
        canttad += cantvad
        print("Gracias por su compra, disfrute la función")
    
    cont = input("Para continuar presione enter, para finalizar digite (n): ")
    if cont.lower() == "n":
        break

ventt = ventad + ventjo + ventni
porcentni = ventni * 100 / ventt
porcentjo = ventjo * 100 / ventt
porcentad = ventad * 100 / ventt
cantdvv = canttni + canttjo + canttad

if cont.lower() == "n":
    print("Cantidad de boletos vendidos categoría niño:", canttni, "Porcentaje del total de ventas: {:.1f}%".format(porcentni))
    print("Cantidad de boletos vendidos categoría joven:", canttjo, "Porcentaje del total de ventas: {:.1f}%".format(porcentjo))
    print("Cantidad de boletos vendidos categoría adulto:", canttad, "Porcentaje del total de ventas: {:.1f}%".format(porcentad))
    print("Cantidad de boletos vendidos:", cantdvv)
    print("Monto total recaudado: $", ventt)