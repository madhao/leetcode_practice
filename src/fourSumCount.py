"""LeetCode coding example."""
from typing import List
from collections import Counter


def fourSumCount(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    """Code to generate total number of combinations =0.

    Args:
        A (List[int]): 1st list
        B (List[int]): 2nd list
        C (List[int]): 3rd list
        D (List[int]): 4th list

    Returns:
        int: count of sum as 0
    """
    counter = 0
    X = [a + b for a in A for b in B]
    Y = [c + d for c in C for d in D]

    ys = Counter(Y)

    for v in X:
        if -v in ys:
            counter += ys[-v]

    return counter


if __name__ == "__main__":
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(fourSumCount(A, B, C, D))
