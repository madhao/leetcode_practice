"""LeetCode coding example."""
from typing import List
from collections import Counter, defaultdict


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
    # counter = 0
    # X = [a + b for a in A for b in B]
    # Y = [c + d for c in C for d in D]

    # ys = Counter(Y)

    # for v in X:
    #     if -v in ys:
    #         counter += ys[-v]
    # this code is from leetcode and is fasster than the code above as it does not have a n^2 complexity but lower
    A, B, C, D = Counter(A), Counter(B), Counter(C), Counter(D)

    first = defaultdict(int)
    for i in A:
        for j in B:
            first[i + j] += A[i] * B[j]
    counter = 0
    for c in C:
        for d in D:
            if -(c + d) in first:
                counter += first[-(c + d)] * C[c] * D[d]

    return counter


if __name__ == "__main__":
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(fourSumCount(A, B, C, D))
