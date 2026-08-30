"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 1:
            return True

        intervals.sort(key=lambda item:item.start)
        for index, interval in enumerate(intervals):
            if index >= len(intervals) -1:
                return True
            
            old_start, old_end = intervals[index].start, intervals[index].end
            current_s, current_e = intervals[index + 1].start, intervals[index + 1].end

            if current_s < old_end:
                return False

        return True