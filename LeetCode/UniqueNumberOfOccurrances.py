# Number of Unique Occurrances problem: https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = []
        
        for i in set(arr):
            count = arr.count(i)
            
            if count in counts:
                return False
            else:
                counts.append(count)
            
        return True
