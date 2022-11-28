def numero_primo(numero, aux):
    if numero > 1:
        if aux < 2:
            return 'Numero primo'
        if numero % aux == 0:
            return None
        else:
            return numero_primo(numero, aux - 1)
    else: return None
print(numero_primo(2, 2-1))