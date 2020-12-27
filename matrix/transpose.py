import unittest


def transpose(matrix):
    rowLen = len(matrix)
    columLen = len(matrix[0])

    new = [None] * columLen

    for index, row in enumerate(new):
        new[index] = [None] * rowLen

    for rowIndex, row in enumerate(matrix):
        for columnIndex, column in enumerate(row):
            new[columnIndex][rowIndex] = column
    return new


class TestTranspose(unittest.TestCase):

    def test_1_3(self):
        m1_3 = [[1, 2, 3]]
        m3_1 = [
            [1],
            [2],
            [3]
        ]
        self.assertEqual(transpose(m1_3), m3_1, "Should be transpose")

    def test_2_3(self):
        m2_3 = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        m3_2 = [
            [1, 4],
            [2, 5],
            [3, 6]
        ]
        self.assertEqual(transpose(m2_3), m3_2, "Should be transpose")

    def test_2_3(self):
        m3_3 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        m3_32 = [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]
        self.assertEqual(transpose(m3_3), m3_32, "Should be transpose")


if __name__ == '__main__':
    unittest.main()
