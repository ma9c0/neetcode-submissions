class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_s, new_e = newInterval[0], newInterval[1]

        res = []
        merged = False
        for interval in intervals:

            start, end = interval[0], interval[1]
            
            # not at merge position yet
            if new_s > end:
                res.append(interval)
            elif new_e < start:
                if not merged:
                    res.append([new_s, new_e])
                    merged = True
                res.append(interval)
            else:
                new_s = min(new_s, start)
                new_e = max(new_e, end)

        if not merged:
            res.append([new_s, new_e])
        
        return res

        