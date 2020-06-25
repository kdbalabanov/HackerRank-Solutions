# Longest Substring Without Repeating Characters problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_s = ''
        max_length = 0
        
        for c in s:
            if c in sub_s:
                sub_s = sub_s[sub_s.index(c)+1:]
            
            sub_s += c
            max_length = max(len(sub_s), max_length)
        
        return max_length
