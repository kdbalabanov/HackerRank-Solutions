# Sort Array by Parity problem: https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        result = []
        
        for element in A:
            if element % 2 == 0:
                result[:0] = [element]
            else:
                result += [element]
        
        return result
