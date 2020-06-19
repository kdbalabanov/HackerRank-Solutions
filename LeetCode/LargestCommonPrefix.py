# Largest Common Prefix: https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        
        if not strs:
            return result
        
        for x in zip(*strs):
            if len(set(x)) == 1:
                result += x[0]
            else:
                return result
        
        return result
