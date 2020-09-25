# Matrix Diagonal Sum problem: https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        matrix_length = len(mat)
        
        for i in range(0, matrix_length):
            if (matrix_length % 2 != 0) and (i == (matrix_length - 1)//2):
                result += mat[i][i]
            else:
                result += mat[i][i]
                result += mat[i][-i - 1]
        
        return result
