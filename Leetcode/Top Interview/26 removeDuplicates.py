class Solution:
    def __init__(self, nums: list[int]) -> int:
        nums [:] = list(set(nums))
        print(nums)


prueba = Solution([1,1,2])