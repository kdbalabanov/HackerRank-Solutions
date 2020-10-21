# Maximum Nesting Depth of Parentheses problem: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        parentheses = []
        count = 0
        depth = 0
        
        if '(' not in s:
            return 0
        
        for c in s:
            if c == '(':
                count += 1
                parentheses.append(c)
                depth = max(count, depth)
            elif c == ')':
                count -= 1
                parentheses.pop()
        
        return depth
