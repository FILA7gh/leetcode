class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        array_1_values, array_2_values = {}, {}
        for i in nums1:
            array_1_values[i] = 1
        for i in nums2:
            array_2_values[i] = 1

        array_1, array_2 = [], []

        for i in array_1_values.keys():
            if not array_2_values.get(i):
                array_1.append(i)

        for i in array_2_values.keys():
            if not array_1_values.get(i):
                array_2.append(i)

        return [array_1, array_2]