# Merge strings alternatively problem: https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_one_len = len(word1)
        word_two_len = len(word2)
        max_len = max(word_one_len, word_two_len)
        result = ''
        
        for i in range(0, max_len):
            if word_one_len > i:
                result += word1[i]
            if word_two_len > i:
                result += word2[i]
        
        return result
