vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]
acum = 0

for  index in range(len(vector1)):
    acum += (vector1[index]*vector2[index])
print (f'Result: {acum}')