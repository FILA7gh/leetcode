class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        counter = 0
        for i in range(1, len(arr) + k + 1):
            if i not in arr:
                counter += 1
            if counter == k:
                counter = i
                break

        return counter
