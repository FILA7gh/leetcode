class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        peoples_dict = {heights[i]: names[i] for i in range(len(names))}
        sorted_names = []
        for i in sorted(heights, reverse=True):
            sorted_names.append(peoples_dict[i])
        return sorted_names
