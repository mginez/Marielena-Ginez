matriz_A = [ [1, 2, 3], [4, 5, 6] ]
matriz_B = [ [-1, 0], [0, 1], [1, 1] ]
a, b = 0, 0
count = 0
count2 = 0

for fila in matriz_A:
    for i in matriz_A[count2]:
        a += i * matriz_B[count][0]
        b += i * matriz_B[count][1]
        count += 1
    print (a, b)
    a, b, count = 0, 0, 0
    count2 += 1
