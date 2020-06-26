# Majority Element problem: https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set(nums)
        
        for num in s:
            if nums.count(num) > len(nums) // 2:
                return num
