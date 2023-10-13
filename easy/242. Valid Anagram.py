class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            return True if sorted(s) == sorted(t) else False
        else:
            return False
