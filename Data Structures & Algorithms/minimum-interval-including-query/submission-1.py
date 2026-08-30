import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        

        res = [-1] * len(queries)

        intervals.sort(key = lambda item:item[0])
        sorted_queries = sorted(enumerate(queries), key = lambda item:item[1])

        rights = []
        interval_pointer = 0
        for index, query in sorted_queries:
            while interval_pointer < len(intervals) and intervals[interval_pointer][0] <= query:
                left, right = intervals[interval_pointer][0], intervals[interval_pointer][1]
                heapq.heappush(rights, (right - left + 1, right))
                interval_pointer += 1

            # pop from rights that right is smaller than query

            while rights and rights[0][1] < query:
                heapq.heappop(rights)

            if not rights:
                continue

            if rights:
                res[index] = rights[0][0]

        return res