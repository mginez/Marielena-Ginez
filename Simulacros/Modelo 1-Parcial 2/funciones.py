def numero_primo(numero, aux):
        if numero > 1:
            if aux < 2:
                return 'Numero primo'
            if numero % aux == 0:
                return None
            else:
                return numero_primo(numero, aux - 1)
        else: return None

def numero_deficiente(numero, divisor, acum):
    if divisor < 1:
        if acum < numero:
            return 'Numero deficiente'
        else:
            return None
    if numero % divisor == 0:
        acum += divisor
    return numero_deficiente(numero, divisor - 1, acum)