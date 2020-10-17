from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
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
    arr = [
        1,
        2,
        3,
        4,
    ]
    print(productExceptSelf(arr))
