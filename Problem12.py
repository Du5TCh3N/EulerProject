# What is the value of the first triangle number to have over five hundred divisors?
num = 0
x = 1
factors = []

while len(factors) < 500:
    num += x
    print(num)
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    x += 1
print(num, factors)
