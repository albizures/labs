import unittest


def getMatrixOrder(matrix):
    rowLen = len(matrix)
    columLen = len(matrix[0])

    return [rowLen, columLen]


class TestTranspose(unittest.TestCase):

    def test_1_3(self):
        m1_3 = [[1, 2, 3]]
        m2_3 = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        self.assertEqual(getMatrixOrder(m1_3), [1, 3], "Should get 1, 3")
        self.assertEqual(getMatrixOrder(m2_3), [2, 3], "Should get 2, 3")


if __name__ == '__main__':
    unittest.main()
