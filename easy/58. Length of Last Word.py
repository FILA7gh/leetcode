class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        s = s[::-1]
        for i in s.lstrip():
            if i == ' ':
                break
            counter += 1

        return counter