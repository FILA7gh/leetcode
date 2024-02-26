class Solution:
    def frequencySort(self, s: str) -> str:
        counter_dict = {}
        result = ''

        for i in s:
            if counter_dict.get(i, None) is not None:
                counter_dict[i] += 1
            else:
                counter_dict[i] = 1

        for i in sorted(counter_dict.items(), key=lambda x: x[1], reverse=True):
            result += i[0] * i[1]
        return result
