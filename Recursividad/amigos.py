def numeros_amigos(num1, num2, div1, div2, acum1, acum2):
    if div1 < 1 and div2 < 1:
        if num1 == acum2 and num2 == acum1:
            return 'Son panas'
        else:
            return None
    if div1 > 0 and num1 % div1 == 0:
        acum1 += div1
    if div2 > 0 and num2 % div2 == 0:
        acum2 += div2
    return numeros_amigos(num1, num2, div1-1, div2-1, acum1, acum2)

print(numeros_amigos(220, 284, 220-1, 284-1, 0, 0))
