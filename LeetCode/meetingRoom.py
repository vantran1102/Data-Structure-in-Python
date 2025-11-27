from typing import List
class Interval(object):
    def __init_(self,start,end):
        self.start = start
        self.end = end
class Solution:
    def canAttendMeetings(self,intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for prev, curr in zip(intervals, intervals[1:]):
            if prev[1] > curr[0]:
                return False
        return True
        
my_meetings = [[0,30],[5,10],[15,20]]
print(Solution().canAttendMeetings(my_meetings))
my_meeting2=[(5,8),(9,15)]
print(Solution().canAttendMeetings(my_meeting2))