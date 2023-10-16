class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        seconds = 0
        for i in range(len(timeSeries) - 1):
            dur = timeSeries[i+1] - (timeSeries[i])
            if duration <= dur:
                seconds += duration
            else:
                seconds += dur
        return seconds + duration
