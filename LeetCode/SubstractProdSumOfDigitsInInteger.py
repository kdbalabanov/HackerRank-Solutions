# Substract product and sum of digits in integer problem: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

import math

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = list(map(int, list(str(n))))        
        return math.prod(nums) - sum(nums)
