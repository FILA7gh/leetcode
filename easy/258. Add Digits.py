class Solution:
    def addDigits(self, num: int) -> int:
        count = 0
        for i in str(num):
            count += int(i)
        if len(str(count)) == 1:
            return count
        else:
            return Solution.addDigits(self, count)
