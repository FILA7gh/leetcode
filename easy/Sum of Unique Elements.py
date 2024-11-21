class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = 0
        unique_dict = {}
        for i in nums:
            if not unique_dict.get(i):
                counter += i
                unique_dict[i] = 1
            else:
                if unique_dict.get(i) == 1:
                    counter -= i
                    unique_dict[i] += 1
        return counter
    