#Which starting number, under one million, produces the longest chain?
chain = []
length = 0
max = [0, 0]

for i in range(1, 1000000):
    n = i
    chain = [i]
    running = True
    while running:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        chain.append(int(n))
        if n == 1:
            running = False
    if len(chain) > max[1]:
        max = [i, len(chain)]
print(max)
