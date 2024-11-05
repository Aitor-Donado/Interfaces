# -*- coding: utf-8 -*-

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplica(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Err"
    return num1/num2

def porcentaje(num1, num2):
    return num1 * num2 / 100

operaciones = {"sumar": lambda num1, num2: num1 + num2, 
               "restar": resta, 
               "dividir": divide, 
               "multiplicar": multiplica, 
               "porcentaje": porcentaje}

def calcula(operando1, operacion, operando2):
    if operando1 == "":
        num1 = 0
    else:
        num1 = float(operando1)
    num2 = float(operando2)
    resultado = operaciones[operacion](num1, num2)
    if resultado == "Err":
        return "Err"
    resultado = round(resultado,9)
    if resultado == int(resultado):
        resultado = int(resultado)
    return str(resultado)[:9]


