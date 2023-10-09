class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        if len(res) > 0:
            return [res[0], res[-1]]
        return [-1, -1]

