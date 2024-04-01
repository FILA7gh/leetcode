class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        data_dict = {}
        output_list = []
        for num in nums:
            if data_dict.get(num, None):
                data_dict[num] += 1
            else:
                data_dict[num] = 1
        for key, value in data_dict.items():
            if value == 1:
                output_list.append(key)
        return output_list
