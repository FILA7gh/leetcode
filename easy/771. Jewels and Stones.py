class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num = 0
        for i in jewels:
            for j in stones:
                if i == j:
                    num += 1
        return num
