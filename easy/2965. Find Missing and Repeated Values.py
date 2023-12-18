class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        extended_list = []
        for i in grid:
            extended_list.extend(i)
        grid_dict = {}
        answer = []
        for i in extended_list:
            if not grid_dict.get(i):
                grid_dict[i] = 1
            else:
                answer.append(i)
        for i in range(1, len(grid_dict) + 2):
            if not grid_dict.get(i):
                answer.append(i)
        return answer
