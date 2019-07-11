Matrix = []
with open('Problem 82 matrix.txt') as f:
    for line in f:
        Matrix.append([int(i) for i in line.rstrip('\n').split(",")])
print(Matrix)
testMatrix = [[131, 673, 234, 103, 18],
              [201, 96, 342, 965, 150],
              [630, 803, 746, 422, 111],
              [537, 699, 497, 121, 956],
              [805, 732, 524, 37, 331]]

def dijkstraAlgorithm(matrix, length):
    m = [[0 for i in range(length)] for j in range(length)]
    '''
    for x in range(0, length):
        for y in range(0, length):
            m[x][y] = matrix[x][y]
    '''
    for y in range(length):
        m[y][0] = matrix[y][0]
    x, y = 0, 0
    while x != length:
        while y != length:



            y += 1
        x += 1
    return m



result = dijkstraAlgorithm(testMatrix, len(testMatrix))
print('\n'.join([', '.join(['{:4}'.format(item) for item in row])
      for row in result]))
