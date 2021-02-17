# 1 2 3 4 5
# 2 1 2 3 4
# 3 2 1 2 3
# 4 3 2 1 2
# 5 4 3 2 1


size = int(input("Size: "))
matrix = []

for row in range(size):
    matrix.append([None] * size)

for deep in range(size):
    for index in range(size - deep):
        matrix[index + deep][index] = deep + 1
        matrix[index][index + deep] = deep + 1

for row in matrix:
    print(row)
