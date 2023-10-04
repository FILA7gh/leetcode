class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        lst = [2**i for i in range(31)]
        return True if n in lst else False