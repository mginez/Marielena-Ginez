from primo import numero_primo

def numero_poderoso(numero, aux, divisores_primos, divisores_noprimos):
    
    if aux < 1:
        if divisores_noprimos == [] or divisores_primos == []:
            return None
        else:
            for div_noprimo in divisores_noprimos:
                for div_primo in divisores_primos:
                    if div_noprimo%div_primo == 0:
                        return 'Numero perfecto'
            return None
    if numero % aux == 0 and numero_primo(aux, aux-1):
        divisores_primos.append(aux)
    elif numero % aux == 0 and not numero_primo(aux, aux-1):
        divisores_noprimos.append(aux)
    return numero_poderoso(numero, aux - 1, divisores_primos, divisores_noprimos)

print(numero_poderoso(25, 25-1, [], []))