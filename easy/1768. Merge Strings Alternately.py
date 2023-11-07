class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ''
        lw1, lw2 = len(word1), len(word2)
        min_len = min(lw1, lw2)
        for i in range(min_len):
            word += word1[i]
            word += word2[i]
        if lw1 < lw2:
            word += word2[min_len:]
        elif lw2 < lw1:
            word += word1[min_len:]
        return word
