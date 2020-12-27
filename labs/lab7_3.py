# find the column within the matrix
# with maximum number of zeros
# and move it to the start of matrix

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


rows = int(input("Enter how many rows (int): "))
columns = int(input("Enter how many columns (int): "))

matrix = []
zeros_by_column = [0] * columns
for column in range(rows):
    matrix.append([])
    for row in range(columns):
        value = float(input("Enter the {} column {} row: ".format(row + 1, column + 1)))
        matrix[column].append(value)
        if value == 0:
            zeros_by_column[column] += 1
