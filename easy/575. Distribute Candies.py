class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        candies = len(candyType) // 2
        types = len(set(candyType))
        if types <= candies:
            return types
        else:
            return candies
