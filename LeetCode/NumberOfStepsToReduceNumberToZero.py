# Number of Steps to Reduce Number to Zero problem: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps (self, num: int) -> int:
        result = 0
        
        while num > 0:
            if num % 2 != 0:
                num -= 1
            else:
                num /= 2
            
            result += 1
        
        return result
