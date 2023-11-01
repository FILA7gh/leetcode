class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums = sorted(nums)
        arr = []
        for i in range(0,len(nums),2):
            arr.append(nums[i])
        return sum(arr)
