def numero_ambicioso(numero, divisor, acum):
    
    if divisor < 1 and acum > 0:
        if acum != numero:
            return numero_ambicioso(acum, acum-1, 0)
        elif acum == numero:
            return 'Ambicioso'
    elif divisor < 1 and acum < 1:
        return None

    if numero % divisor == 0:
        acum += divisor
    return numero_ambicioso(numero, divisor - 1, acum)

print(numero_ambicioso(25, 25-1, 0))