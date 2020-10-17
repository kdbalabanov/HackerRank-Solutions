# Self Dividing Numbers problem: https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [x for x in range(left, right + 1) if self.isSelfDividing(x)]
    
    def isSelfDividing(self, num: int) -> bool:
        for digit in str(num):
            current = int(digit)
            if (current == 0) or (num % current != 0):
                return False
        
        return True
