# Roman to Integer problem: https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = []
        
        for x in range(0, len(s)):
            current = roman_values[s[x]]
            
            if len(result) == 0:
                result.append(current)
            else:
                prev = result[-1]
                
                if current > prev:
                    result[-1] = prev * -1
                    
                result.append(current)
        
        return sum(result)
