# N Repeated Element In Size 2N Array problem: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dictionary = {}
        
        for element in A:
            if element in dictionary.keys():
                return element
            else:
                dictionary[element] = 1
