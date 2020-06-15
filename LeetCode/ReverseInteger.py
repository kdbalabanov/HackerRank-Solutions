# Reverse Integer problem: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        l = list(reversed(str(abs(x))))
        rev = int(''.join(l))
            
        if (abs(rev) > (2 ** 31 - 1)):
            return 0
        
        if x < 0:
            return -rev
        
        return rev