class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda item: item[0])
        res = []

        new_s, new_e = intervals[0][0], intervals[0][1]
        for itv in intervals[1:]:
            if itv[0] <= new_e :
                new_s = min(itv[0], new_s)
                new_e = max(itv[1], new_e)
            else:
                res.append([new_s, new_e])
                new_s, new_e = itv[0], itv[1]

        res.append([new_s, new_e])

        return res