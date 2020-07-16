# Number of good pairs problem: https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequency = {}
        result = 0
        
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
                
        for num in frequency:
            result += frequency[num] * (frequency[num] - 1) // 2
        
        return result