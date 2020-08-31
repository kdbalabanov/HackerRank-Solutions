# Count good tirplets problem: https://leetcode.com/problems/count-good-triplets/

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        length = len(arr)
        result = 0
        
        for i in range(length):
            for k in range(i + 1, length):
                if abs(arr[i] - arr[k]) <= c:
                    result += sum(abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b for j in range(i + 1, k))
                
        return result