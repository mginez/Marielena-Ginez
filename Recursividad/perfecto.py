
def numero_perfecto(numero, divisor, acum):
    if divisor < 1:
        if acum == numero:
            return 'Numero perfecto'
        else:
            return None
    if numero % divisor == 0:
        acum += divisor
    return numero_perfecto(numero, divisor - 1, acum)

print(numero_perfecto(6, 6-1, 0))
