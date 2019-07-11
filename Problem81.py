Matrix = []
with open('Problem 81 matrix.txt') as f:
    for line in f:
        Matrix.append([int(i) for i in line.rstrip('\n').split(",")])

testMatrix = [[131, 673, 234, 103, 18],
              [201, 96, 342, 965, 150],
              [630, 803, 746, 422, 111],
              [537, 699, 497, 121, 956],
              [805, 732, 524, 37, 331]]

def dijkstraAlgorithm(matrix, length):
    m = [[0 for i in range(length)] for j in range(length)]
    for x in range(0, length):
        for y in range(0, length):
            if x == 0 and y == 0:
                m[0][0] = matrix[0][0]
            elif x == 0:
                m[x][y] = m[x][y-1] + matrix[x][y]
            elif y == 0:
                m[x][y] = m[x-1][y] + matrix[x][y]
            else:
                m[x][y] = min(m[x-1][y], m[x][y-1]) + matrix[x][y]

    return m



result = dijkstraAlgorithm(Matrix, len(Matrix))
print('\n'.join([', '.join(['{:4}'.format(item) for item in row])
      for row in result]))
