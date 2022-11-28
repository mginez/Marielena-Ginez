
def exponential(base, exp):
    if exp == 0:
        return 1
    return base * exponential(base, exp-1)

def main():

    n = int(input('Numero: '))
    exp = int(input('Exponente: '))

    exponential(n, exp)

main()