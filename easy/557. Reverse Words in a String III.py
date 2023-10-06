class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = []
        for word in s.split():
            new_s.append(word[::-1])
        return ' '.join(new_s)
