# Two Sum II Input Array Is Sorted problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = {}
        
        for i in range(0, len(numbers)):
            diff = target - numbers[i]
            
            if diff in result:
                return [result[diff]+1, i+1]
            
            result[numbers[i]] = i
