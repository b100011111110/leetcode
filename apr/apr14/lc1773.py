from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        c = 0
        for i,j,k in items:
            if ruleKey == "type" and ruleValue == i:
                c += 1
            elif ruleKey == "color" and ruleValue == j:
                c += 1
            elif ruleKey == "name" and ruleValue == k:
                c += 1
        return c