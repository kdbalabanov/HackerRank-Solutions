# Add Binary problem: https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = 0
        result = ''
        carry = '0'
        
        while i < max(len(a), len(b)) or carry == '1':
            a_num = a[-1 - i] if i < len(a) else '0'
            b_num = b[-1 - i] if i < len(b) else '0'
            
            calc = int(a_num) + int(b_num) + int(carry)
            result = str(calc % 2) + result
            
            carry = '1' if calc > 1 else '0'
            i += 1
        
        return result
