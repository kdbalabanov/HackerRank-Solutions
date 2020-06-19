# Balanced Parantheses problem: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        opening_brackets = '([{'
        
        for c in s:
            if c in opening_brackets:
                l.append(c)
            else:
                if not l:
                    return False
                
                prev = l.pop()
                
                if (prev == '(' and c == ')') or (prev == '[' and c == ']') or (prev == '{' and c == '}'):
                    continue
                else:
                    return False
        
        return not l
