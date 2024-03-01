class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_dict = {}
        for i in nums:
            if nums_dict.get(i):
                del nums_dict[i]
            else:
                nums_dict[i] = 1
        if nums_dict:
            return False
        return True
