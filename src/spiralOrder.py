"""LeetCode coding example."""
from typing import List
from numpy import array


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    """Code to find answer to spiralOrder traversal of a m*n matrix.

    Question: https://leetcode.com/problems/spiral-matrix/

    Args:
        matrix (List[List[int]]): m*n matrix

    Returns:
        List[int]: spiral order traversal of input m*n matrix
    """
    matrix = array(matrix)
    res = []
    while 1:
        if len(matrix) > 0 and len(matrix[0]) > 0:
            m = len(matrix)
            n = len(matrix[0])
        else:
            break
        if (m > 1) & (n > 1):
            for e in range(n):
                res.append(matrix[0][e])
            for e in range(1, m):
                res.append(matrix[e][n - 1])
            for e in reversed(range(n - 1)):
                res.append(matrix[m - 1][e])
            for e in reversed(range(1, m - 1)):
                res.append(matrix[e][0])
            matrix = matrix[1 : m - 1, 1 : n - 1]  # noqa: E203
        elif (m > 1) & (n == 1):
            for e in range(m):
                res.append(matrix[e][0])
            break
        elif (m == 1) & (n > 1):
            for e in range(n):
                res.append(matrix[0][e])
            break
        elif (m == 1) & (n == 1):
            res.append(matrix[0, 0])
            break
        else:
            break
    return res


if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(spiralOrder(arr))
