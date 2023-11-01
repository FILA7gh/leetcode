class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        word1, word2 = ''.join(word1), ''.join(word2)
        return True if word1 == word2 else False
    