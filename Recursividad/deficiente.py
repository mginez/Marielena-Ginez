def numero_deficiente(numero, divisor, acum):
    if divisor < 1:
        if acum < numero:
            return 'Numero deficiente'
        else:
            return None
    if numero % divisor == 0:
        acum += divisor
    return numero_deficiente(numero, divisor - 1, acum)

print(numero_deficiente(12, 12-1, 0))