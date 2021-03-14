# Maximum number of balls in a box problem: https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

class Solution: 
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        results = {}
        
        for n in range(lowLimit, highLimit + 1):
            boxNum = 0
            
            while n:
                boxNum = boxNum + n % 10
                n = n // 10
                
            if boxNum not in results:
                results[boxNum] = 1
            else:
                results[boxNum] += 1
        
        return max(results.values())
