#si el numero esta y la posicion
def fibonacci(numero, aux, aux2, count):
    acum = aux + aux2
    if acum < numero:
        count += 1
        return fibonacci(numero, aux2, acum, count)
    elif acum == numero:
        count += 1
        return count
    else:
        None
#11235813
print(fibonacci(5, 1, 1, 2))