class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            max_height = min(height[l], height[r])
            if max_height * (r - l) > max_area:
                max_area = max_height * (r - l)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
