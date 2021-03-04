# Count items matching a rule problem: https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleKeys = {'type': 0, 'color': 1, 'name': 2}
        return sum(1 for item in items if item[ruleKeys[ruleKey]] == ruleValue)
