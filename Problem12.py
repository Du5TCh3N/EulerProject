# What is the value of the first triangle number to have over five hundred divisors?

#Brute force Method
'''
num = 0
x = 1
factors = []

while len(factors) < 500:
    num += x
    print(num, len(factors))
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    x += 1
print(num, factors)
'''

#Algorithmic approach
def num_divisors(n):
    if n % 2 == 0: n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors

def find_triangular_index(factor_limit):
    n = 1
    lnum, rnum = num_divisors(n), num_divisors(n+1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, num_divisors(n+1)
    return n

index = find_triangular_index(500)
triangle = (index * (index + 1)) / 2

print(triangle)
