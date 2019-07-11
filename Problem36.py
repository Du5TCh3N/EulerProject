def reverse(s):
    r = ""
    for c in s:
        r = c + r
    return str(r)

def binary(s):
    r = bin(s)[2:]
    return r

m = 0
for n in range(1000000):
    decRight = str(n)
    decReverse = reverse(decRight)
    binRight = str(binary(n))
    binReverse = reverse(binRight)
    if decRight == decReverse and binRight == binReverse:
        print(n)
        m += 1

print(m)
