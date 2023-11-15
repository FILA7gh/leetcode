class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        nums_count = []
        counter = 0
        for i in nums:
            if i == 1:
                counter += 1
            elif i == 0:
                nums_count.append(counter)
                counter = 0
        nums_count.append(counter)
        return max(nums_count)
