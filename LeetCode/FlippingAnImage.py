# Flipping an Image problem: https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for index, row in enumerate(A):
            A[index] = [1 if x == 0 else 0 for x in row[::-1]]
        return A
