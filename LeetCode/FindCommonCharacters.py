# Find Common Characters problem: https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = []
        
        for c in set(A[0]):
            
            for i in range(0, min(set(s.count(c) for s in A))):
                result.append(c)
        
        return result
