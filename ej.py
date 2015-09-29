def ingreso():
    corte = 1
    while (corte == 1):
        mi_nombre = raw_input("digite:")
        print mi_nombre
        print "continuar?"
        corte = input("digite:")

def main():
    print "elija una opcion"
    opcion = input("digite:")
    if (opcion == 1):
        ingreso()

main()
