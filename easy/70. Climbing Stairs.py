class Solution:
    def climbStairs(self, n: int) -> int:
        counter_one = 1
        counter_two = 2
        if n == 1:
            return 1
        elif n == 2:
            return 2

        for i in range(n-2):
            counter_two += counter_one
            counter_one = counter_two - counter_one

        return counter_two
