class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        swap_dict = {}
        for i in range(len(s)):
            swap_dict[s[i]] = t[i]
        string = ''
        for i in s:
            string += swap_dict[i]
        if len(swap_dict) != len(set(swap_dict.values())):
            return False

        return string == t