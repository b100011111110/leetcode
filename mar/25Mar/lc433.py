from typing import List
from collections import defaultdict

class Solution:
    def minMutation(self, st: str, en: str, bank: List[str]) -> int:
        def diff(w1,w2):
            c = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    c += 1
            return c == 1

        bank.append(st)
        map = defaultdict(list)
        for i in range(len(bank)):
            for j in range(i+1,len(bank)):
                if diff(bank[i],bank[j]):
                    map[bank[i]].append(bank[j])
                    map[bank[j]].append(bank[i])

        ans = 0
        que = [(st,0)]
        visited = set()
        while que:
            word,c = que.pop(0)
            if word in visited:
                continue
            visited.add(word)
            for j in map[word]:
                que.append((j,c+1))
            if word == en:
                return c
        return -1