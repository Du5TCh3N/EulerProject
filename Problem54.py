Cards = []
def readCards(Cards):
    with open('Problem 54 poker.txt') as f:
        for line in f:
            Cards.append([str(line).strip('\n')])
    return Cards
Cards = readCards(Cards)

def __main__():
    for x in range(1000):
        
