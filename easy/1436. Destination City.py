class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        paths_dict = {}
        for i in paths:
            paths_dict[i[0]] = i[1]
        for i in paths_dict.values():
            if not paths_dict.get(i):
                return i
