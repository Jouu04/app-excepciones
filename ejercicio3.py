while(True):
    try:
        numero = float(input("Ingrese un numero :"))
        resultado = "IMPAR"
        if (numero % 2 == 0):
            resultado = "PAR"
        print("El número {} es {}".format(numero,
                                          resultado))
        break
    except:
        print("Ocurrio un error!!")