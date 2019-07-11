number = []
value = int(0)
with open('Problem 13 Largest sum.txt') as f:
    for line in f:
        number.append(int(line))
print(number)
for x in range(len(number)):
    value += number[x]
print(value)
