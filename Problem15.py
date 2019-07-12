#Starting in the top left corner of a 20x20 grid, and only being able to move to the right and down, how many such routes are there to reach the bottom right corner.
num = 3
current = 6
gridSize = [num,num]
correct = 137846528820


def recPath(gridSize):
    #Recursive solution to grid problem. Input is a list of x,y moves remaining.
    #if base case, no moves left
    if gridSize == [num - 1, num - 1]:
        return current

    #recursive calls
    paths = 0
    #move left when possible
    if gridSize[0] > 0:
        paths += recPath([gridSize[0] - 1, gridSize[1]])
    #move down when possible
    if gridSize[1] > 0:
        paths += recPath([gridSize[0], gridSize[1] - 1])

    return paths

def route_num(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[cube_size - 1]

n = route_num(20)
print(n)
