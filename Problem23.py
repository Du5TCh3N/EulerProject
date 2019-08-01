def sum_divisors(n):
    s = 0
    for i in range(1,n):
        if n % i == 0: s += i
    return s
l = []
def createL():
    S = 0
    for i in range(1, 28124):
        if sum_divisors(i) > i:
            l.append(i)
            for n in l:
                s = n + i
                print(s, "=", n, "+", i)
                S += s
    print(S)
createL()
