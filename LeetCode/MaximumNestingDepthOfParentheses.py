# Maximum Nesting Depth of Parentheses problem: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        depth = 0
        
        for c in s:
            if c == '(':
                count += 1
                depth = max(count, depth)
            elif c == ')':
                count -= 1
        
        return depth
