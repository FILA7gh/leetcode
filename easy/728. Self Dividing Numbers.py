class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lst = []
        for i in range(left, right+1):
            new_i = ''
            for k in str(i):
                if int(k) != 0:
                    if i % int(k) == 0:
                        new_i += k
            if str(i) == new_i:
                lst.append(i)
        return lst
