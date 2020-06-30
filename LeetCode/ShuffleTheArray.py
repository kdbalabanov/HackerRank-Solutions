# Shuffle The Array problem: https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [element for pair in list(zip(nums[:n], nums[n:])) for element in pair]
