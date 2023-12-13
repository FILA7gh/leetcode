class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        index = 0
        while index != len(s):
            some_list = []

            for i in s[index:]:
                if i not in some_list:
                    some_list.append(i)
                    max_count = max(max_count, len(some_list))
                else:
                    break
            index += 1
        return max_count
