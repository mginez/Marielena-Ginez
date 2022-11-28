def fibonacci(numero, aux, aux2):
    acum = aux + aux2
    if acum < numero:
        return fibonacci(numero, aux2, acum)
    elif acum == numero:
        return True
    else:
        None

def numero_primo(numero, aux):
    if numero > 1:
        if aux < 2:
            return 'Numero primo'
        if numero % aux == 0:
            return None
        else:
            return numero_primo(numero, aux - 1)
    else: return None

