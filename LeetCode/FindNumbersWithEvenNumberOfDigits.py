# Find numbers with even number of digits problem: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        nums_str = map(str, nums)
        return sum([1 for x in nums_str if len(x) % 2 == 0])
