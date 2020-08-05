# Destination city problem: https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        result = {}
        
        for path in paths:
            if path[0] not in result:
                result[path[0]] = 1
            else:
                result[path[0]] += 1
            
            if path[1] not in result:
                result[path[1]] = 0
        
        return min(result, key = result.get)
