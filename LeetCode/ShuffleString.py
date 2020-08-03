# Shuffle string problem: https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [None] * len(s)
        
        for i in range(0, len(s)):
            result[indices[i]] = s[i]
        
        
        return ''.join(result)
