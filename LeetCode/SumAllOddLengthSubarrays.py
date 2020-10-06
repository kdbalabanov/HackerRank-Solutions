# Sum All Odd Length Subarrays problem: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arr_len = len(arr)
        odds = [x for x in range(1, arr_len + 1) if x % 2 != 0]
        result = 0
        
        for odd in odds:
            if odd == 1:
                result += sum(arr)
            else:
                for i in range(0, arr_len):
                    if i + odd <= arr_len:
                        result += sum(arr[i:i+odd])
        
        return result
