class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        m_list = []
        for word in words:
            counter = 0
            for i in words:
                if word in i:
                     counter += 1
            if counter > 1:
                m_list.append(word)
        return m_list
