"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 1:
            return 1

        intervals.sort(key = lambda item: item.start)

        rooms = []

        for index, interval in enumerate(intervals):

            current_start, current_end = intervals[index].start, intervals[index].end

            if rooms and rooms[0] <= current_start:
                heapq.heappop(rooms)

            heapq.heappush(rooms, current_end)

        return len(rooms)
