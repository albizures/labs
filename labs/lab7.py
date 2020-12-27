# Альбисурес дель Валье Хосе Альфредо
# ИУ7-15Б
# седьмая лаборатория

from random import randrange
from math import cos


def printMatrix(matrix, msg):
    length = len(matrix[0])
    print(msg)
    print(" ---------" * length)
    for row in matrix:
        for cell in row:
            if abs(cell) < 1e-4 and cell != 0:
                print("|{:^8e}".format(cell), end=" ")
            else:
                print("|{:^8}".format(round(cell, 3)), end=" ")
        print('|')
    print(" ---------" * length)
    print()


while True:
    size = int(input("Enter the size of the matrix: "))
    if size > 8:
        print("The size must be less than 9")
    else:
        break

d_matrix = []
for column in range(size):
    d_matrix.append([])
    for row in range(size):
        d_matrix[column].append(float(input("Enter the {} column {} row: ".format(row + 1, column + 1))))

print()
printMatrix(d_matrix, "D matrix")

d_matrix.reverse()
for index, row in enumerate(d_matrix):
    d_matrix[index] = row[:]
    d_matrix[index].reverse()


print()
printMatrix(d_matrix, "Reversed D matrix")

d = []
columns = 7
rows = 13
cells = rows * columns
while len(d) < cells:
    d.append(len(d))

x = 0.5
w_matrix = []
for row in range(rows):
    w_matrix.append([])
    for column in range(columns):
        j = row * columns + column
        w_matrix[row].append(cos(d[j]) * x**(1/3))
        x += 0.2

printMatrix(w_matrix, 'W matrix')

b_vector = []


def getMaxMinProduct(arr):
    min_product = max_product = prev_min = prev_max = current_min = current_max = arr[0]

    for i in range(1, len(arr)):
        value = arr[i]
        temp_max = prev_max * value
        temp_min = prev_min * value
        current_max = max(temp_max, temp_min, value, prev_max)
        current_min = min(temp_max, temp_min, value, prev_max)

        max_product = max(max_product, current_max)
        min_product = min(min_product, current_min)

        prev_max = current_max
        prev_min = current_min

    return (current_min, current_max)


max_products = []
min_products = []

for row in w_matrix:
    min_product, max_product = getMaxMinProduct(row)
    max_products.append(max_product)
    min_products.append(min_product)
max_products.sort(reverse=True)
min_products.sort()


for index in range(rows):
    b_vector.append(min_products[index])
    b_vector.append(max_products[index])


print("B Vector")
for item in b_vector:
    print('  - {:2.3f}'.format(item))


size = 7
third_matrix = []
zeros_by_column = [0] * size
for row in range(size):
    third_matrix.append([])
    for col in range(size):
        value = randrange(0, 5)
        third_matrix[row].append(value)
        if value == 0:
            zeros_by_column[col] += 1

column_to_move = 0

printMatrix(third_matrix, 'Before third matrix')
for col in range(size):
    if zeros_by_column[col] > zeros_by_column[column_to_move]:
        column_to_move = col

if(zeros_by_column[column_to_move] == 0):
    print('There is no zeros in the matrix')
else:
    for row in range(size):
        third_matrix[row] = [third_matrix[row].pop(column_to_move)] + third_matrix[row]

printMatrix(third_matrix, 'After third matrix')
