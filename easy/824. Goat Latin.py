class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        wowel_list = ['a', 'e', 'i', 'o', 'u']
        words = ''
        maa = 'maa'
        for i in sentence.split():
            if len(i) < 2:
                words += i + maa + ' '
                maa += 'a'
            else:
                if i[0].lower() in wowel_list:
                    words += i + maa + ' '
                    maa += 'a'
                else:
                    words += i[1:] + i[0] + maa + ' '
                    maa += 'a'
        return words.rstrip()
