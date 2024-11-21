class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0
        for i in nums:
            if i < 10:
                double += i
            else:
                 single += i
        return not single == double
