from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = sorted(score,reverse =True)
        dct = {}
        for i in range(len(ranks)):
            dct[ranks[i]] = str(i+1)
        dct[ranks[0]] = "Gold Medal"
        dct[ranks[1]] = "Silver Medal"
        dct[ranks[2]] = "Bronze Medal"
        return [dct[i] for i in score]