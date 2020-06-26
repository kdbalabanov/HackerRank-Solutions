# TwoSum problem: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        
        for i in range(0, len(nums)):
            diff = target - nums[i]
            
            if diff in result:
                return [result[diff], i]
            
            result[nums[i]] = i
