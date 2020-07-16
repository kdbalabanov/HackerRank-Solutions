# Numbers smaller than current number problem: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = sorted(nums)
        return [l.index(x) for x in nums]