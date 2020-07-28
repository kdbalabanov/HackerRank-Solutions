# Number of students doing homework at given time problem: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        
        for time in zip(startTime, endTime):
            if time[0] <= queryTime <= time[1]:
                count += 1
        
        return count
