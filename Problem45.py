a, b, c = 0, 0, 0
def calculateNum(x, y, z):
    a = (x*(x+1))/2
    b = (y*(3*y-1))/2
    c = z*(2*z-1)
    return a, b, c
m = 2
i = m
j = m
k = m
for x in range(i, i + 100000):
    for y in range(j, j + 100000):
        for z in range(k, k + 100000):
            a, b, c = calculateNum(x, y, z)
            if a == b and a == c:
                print(a, x, y, z)
                print('Found')
