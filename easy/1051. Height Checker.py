class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        counter = 0
        right_heights = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != right_heights[i]:
                counter += 1

        return counter
