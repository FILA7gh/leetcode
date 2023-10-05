def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1, nums2 = nums1[:m], nums2[:n]
    nums1.extend(nums2)
    return sorted(nums1)

print(merge([1,2,3,0,0,0], 2, [2,4,3], 1))