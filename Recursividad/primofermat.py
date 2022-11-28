from primo import numero_primo

def primo_fermat(numero, aux, resultado):
    resultado = (2**2**aux) + 1
    if resultado < numero:
        return primo_fermat(numero, aux+1, resultado)
    elif resultado > numero:
        return None
    elif resultado == numero and numero_primo(numero, numero-1): 
        return 'Primo de Fermat'
print(primo_fermat(5, 1, 1))