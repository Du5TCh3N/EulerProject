def recFactorial(n):
    if n == 1:
        n = 1
        return n
    else:
        n = n * recFactorial(n - 1)
        return n

n = 100
n = recFactorial(n)
n = str(n)
sum = 0
for i in range(len(n)):
    sum += int(n[i])

print(sum)
