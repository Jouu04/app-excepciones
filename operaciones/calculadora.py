def sumar(numero1, numero2):
    try:
        resultado = int(numero1) + int(numero2)
    except:
        print("Ingrese solo numeros")
    else: 
        return resultado

def resta(numero1, numero2):
    try:
        resultado = int(numero1) - int(numero2)
    except:
        print("Ingrese solo numeros")
    else: 
        return resultado

def multiplicar(numero1, numero2):
    try:
        resultado = int(numero1) * int(numero2)
    except:
        print("Ingrese solo numeros")
    else: 
        return resultado

def dividir(numero1, numero2):
    try:
        resultado = int(numero1) / int(numero2)
    except ValueError:
        print("Ingrese solo numeros")
    except ZeroDivisionError:
        print("El numero no puede ser divisible entre 0")
    else: 
        return resultado

