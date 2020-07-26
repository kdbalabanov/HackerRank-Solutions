# Maximum 69 number problem: https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        l  = list(str(num))
        
        if '6' in l:
            l[l.index('6')] = '9'
            return ''.join(l)
        else:
            return num
