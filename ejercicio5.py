while(True):
    try:
        numero = int(input("Ingrese un numero : "))
        resultado = "El numero es primo"
        cond = 0
        c = 1
        while (c<numero):
            c+1
        if (numero % c == 0):
            cond+1
        if cond>2:
            break
    except:
        print("Error al ingresar el numero")
    else:
        print("El numero {} es {}".format(numero, resultado))
    finally:
        print("Fin de busqueda")
        