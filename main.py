from operaciones.calculadora import *
num1 = input("Ingrese el primer numero: ")
num2 = input("Ingrese el segundo numero: ")
print("{} + {} = {}".format(num1, num2, sumar(num1, num2)))
print("{} + {} = {}".format(num1, num2, resta(num1, num2)))
print("{} + {} = {}".format(num1, num2, multiplicar(num1, num2)))
print("{} + {} = {}".format(num1, num2, dividir(num1, num2)))