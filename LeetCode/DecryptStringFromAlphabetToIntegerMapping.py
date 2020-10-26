# Dewcrypt String From Alphabet To Integer Mapping problem: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

import string

class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ''
        dictionary = {str(y+1) if y < 9 else str(y+1) + '#' : x for y, x in enumerate(string.ascii_lowercase)}
        i = 0
        
        while i < len(s):
            if '#' not in s[i:i+3]:
                result += dictionary[s[i]]
                i += 1
            else:
                result += dictionary[s[i:i+3]]
                i += 3
        
        return result
