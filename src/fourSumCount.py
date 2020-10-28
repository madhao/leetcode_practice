"""LeetCode coding example."""
from typing import List


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

    for a in A:
        for b in B:
            ab = a + b
            for c in C:
                abc = ab + c
                for d in D:
                    abcd = abc + d
                    if abcd == 0:
                        counter += 1
                    else:
                        continue

    return counter


if __name__ == "__main__":
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(fourSumCount(A, B, C, D))
