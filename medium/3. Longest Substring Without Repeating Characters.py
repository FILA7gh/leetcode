class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        index = 0
        dct = {}
        while index != len(s):
            for i in s[index:]:
                if not dct.get(i):
                    dct[i] = 1
                    max_count = max(max_count, len(dct))
                else:
                    break
            index += 1
            dct.clear()
        return max_count
