def numero_abundante(numero, divisor, acum):
    if divisor < 1:
        if acum > numero:
            return 'Numero abundante'
        else:
            return None
    if numero % divisor == 0:
        acum += divisor
    return numero_abundante(numero, divisor - 1, acum)

print(numero_abundante(12, 12-1, 0))