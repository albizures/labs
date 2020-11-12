size = int(input("Enter the size of the matrix: "))

def printMatrix (matrix):
    length = len(matrix)
    print("-----" * length)
    for col in matrix:
        print(col)
    print("-----" * length)
    print() 

if size > 8:
    print("The size must be less than 9")

else: 
    matrix = []
    for column in range(size):
        matrix.append([])
        for row in range(size):        
            matrix[column].append(float(input("Enter the {} column {} row: ".format(row + 1, column + 1) )))


    newMatrix = matrix[:]
    newMatrix.reverse()
    for index, row in enumerate(newMatrix):
        newMatrix[index] = row[:] 
        newMatrix[index].reverse()

    print()
    print("Original matrix");
    printMatrix(matrix)
    print("Reversed matrix")
    printMatrix(newMatrix)
