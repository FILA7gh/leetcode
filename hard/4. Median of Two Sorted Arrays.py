class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        len_nums = len(nums1)

        if len_nums % 2 == 0:
            return (nums1[len_nums // 2 - 1] + nums1[len_nums // 2]) / 2
        else:
            return nums1[len_nums // 2] / 1
