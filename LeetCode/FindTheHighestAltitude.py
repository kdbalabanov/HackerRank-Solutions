# Find the highest altitude problem: https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        tmp = 0
        result = [0]
        
        for i in gain:
            tmp += i
            result.append(tmp)
            
        return max(result)
