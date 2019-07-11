fibonacci = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
z = 0

while fibonacci[len(fibonacci)-1] <= 4000000:
    fibonacci.append((fibonacci[len(fibonacci)-1] + fibonacci[len(fibonacci)-2]))

for n in range(len(fibonacci)-1):
    if fibonacci[n] % 2 == 0:
        z += fibonacci[n]

print(z)