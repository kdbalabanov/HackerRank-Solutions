# Xor Operation in Array problem: https://leetcode.com/problems/xor-operation-in-an-array/

import functools

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return functools.reduce((lambda x, y: x ^ y), range(start, start + 2*n, 2))
