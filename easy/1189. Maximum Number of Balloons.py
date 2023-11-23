class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bal_list = []
        for i in 'balloon':
            bal_list.append(text.count(i)//2 if i in ['l', 'o'] else text.count(i))

        return min(bal_list)
