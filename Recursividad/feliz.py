from cuadrado import numero_cuadrado

def numero_feliz(numero):
    if int(numero[-1]) == numero_cuadrado(int(numero), 1, 1):
        return 'Numero feliz'
    else: return None
print(numero_feliz(str(25)))