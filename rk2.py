#
# Вводится целое число -- размер квадратной матрицы. Необходимо сформировать
# матрицу следующего вида
# 5   6   7   8   9
# 4  14  15  10   0
# 3  13  11   0   0
# 2  12   0   0   0
# 1   0   0   0   0
# Далее необходимо определить, какая цифра (кроме 0) встречается чаще всего .


size = int(input("Enter size: "))
matrix = []

for column in range(size):
    matrix.append([])
    for row in range(size):
        matrix[column].append(0)

# [4, 0]
# ....
# [0, 0]
# ....
# [0, 4]
# [1, 3]
# [2, 2]
# [3, 1]


axis = 'y'
y = size - 1
x = 0
deep = 0

value = 1


while True:
    input("x: {}, y: {}, axis: {}, deep: {}".format(x, y, axis, deep))

    if -1 < x < size and -1 < y < size:
        matrix[y][x] = value
        value += 1
        for row in matrix:
            print(row)
    # matrix[x][y] = value
    # value += 1

    if axis == 'y':
        y -= 1
    elif axis == 'x':
        x += 1
    elif axis == 'xy':
        x -= 1
        y += 1

    if y < deep and axis == 'y':
        y = deep
        axis = 'x'
        x += 1

    elif x > size - 1 - deep and axis == 'x':
        axis = 'xy'
        x = size - deep - 2
        y += 1
        deep += 1

    elif axis == 'xy' and (x == deep and y == size - 1 - deep):
        axis = 'y'
        y += 1


print("The matrix is: ")
for column in matrix:
    print('  ', column)


numbers = {}
for column in range(size):
    for row in range(size):
        number = matrix[row][column]
        key = str(number)
        if key == '0':
            continue
        if key in numbers.keys():
            numbers[key] = numbers[key] + 1
        else:
            numbers[key] = 1

print(numbers)
