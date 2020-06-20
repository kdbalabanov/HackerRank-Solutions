# Remove Element problem: https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for i in range(0, len(nums)):
            current = nums[i-counter]
            if current == val:
                nums.remove(current)
                counter += 1
        return len(nums)
