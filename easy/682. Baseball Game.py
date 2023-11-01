class Solution:
    def calPoints(self, operations: list[str]) -> int:
        arr = []
        for i in operations:
            if i == "C":
                arr.pop()
            elif i == 'D':
                arr.append(arr[-1]*2)
            elif i == '+':
                arr.append(arr[-1] + arr[-2])
            else:
                arr.append(int(i))
        return sum(arr)
