class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        length = len(nums) / 3
        if len(nums) < 3:
            return list(set(nums))

        mj_list = []
        for num in nums:
            count = nums.count(num)
            if count > length:
                mj_list.append(num)
        return list(set(mj_list))

