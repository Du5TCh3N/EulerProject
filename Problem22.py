Names = []
def readNames(Names):
    with open("Problem22.txt") as n:
        for line in n:
            currentline = line.split(",")
            for char in currentline:
                n = str(char)
                n = n.replace('"', '').replace('\n', '')
                Names.append(n)
readNames(Names)

letToNum = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

Names = sorted(Names)
Final = 0
for name in Names:
    sum = 0
    for char in name:
        sum += letToNum[char]
    total = (Names.index(name) + 1) * sum
    Final += total
print(Final)
