class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        lst = []
        for i in range(len(strs[0])):
            some_list = []
            for k in strs:
                some_list.append(k[i])

            lst.append(some_list)

        counter = 0
        for i in range(len(lst)):
            if lst[i] != sorted(lst[i]):
                counter += 1
        return counter
