# Lucky Numbers In a Matrix problem: https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        lucky_nums = []
        
        for i in range(0, m):
            minimum = min(matrix[i])
            index = matrix[i].index(minimum)
            
            for j in range(0, m):                
                if (matrix[j][index] > minimum):
                    break
                elif (j == m - 1):
                    lucky_nums.append(minimum)
        
        return lucky_nums
