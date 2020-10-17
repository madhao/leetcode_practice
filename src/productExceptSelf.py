"""LeetCode coding example."""
from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    """Code returns a array of all elements in input array withouth itself.

       This returns the result in O(n).
       Question: https://leetcode.com/problems/product-of-array-except-self/

    Args:
        nums (List[int]): List of input elements

    Returns:
        List[int]: List of elements with product iff all remaining elements
    """
    n = len(nums)
    res = [0] * n
    res[0] = 1
    for idx in range(1, n):
        res[idx] = res[idx - 1] * nums[idx - 1]
    mul = 1
    for idx in reversed(range(n)):
        res[idx] = mul * res[idx]
        mul = mul * nums[idx]
    return res


if __name__ == "__main__":
    array = [
        1,
        2,
        3,
        4,
    ]
    print(productExceptSelf(array))
