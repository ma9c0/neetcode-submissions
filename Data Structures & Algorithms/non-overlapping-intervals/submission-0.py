class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda item: item[0])

        res = []
        removed = 0

        if len(intervals) == 1:
            return 0

        last_end = intervals[0][-1]

        for interval in intervals:
            start, end = interval[0], interval[1]

            if start >= last_end:
                res.append(interval)
                last_end = end
            else:
                if end > last_end:
                    removed += 1
                    continue
                else:
                    removed += 1
                    last_end = end

        return removed - 1