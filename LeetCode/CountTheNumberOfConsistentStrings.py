# Count the number of consistent strings problem: https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        return sum(1 for word in words if len(set(word) - allowed_set) == 0)
