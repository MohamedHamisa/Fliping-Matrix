def flippingMatrix(matrix):
    mid = len(matrix) // 2
    find_max = lambda m, x, y: max(m[x][y], m[x][-y - 1], m[-x - 1][y], m[-x - 1][-y - 1])
    return sum([find_max(matrix, x, y) for x in range(mid) for y in range(mid)])
