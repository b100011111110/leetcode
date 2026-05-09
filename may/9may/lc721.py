from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        idchecker = {}
        box = set()
        ID = 0
        ans = []
        for l in accounts:
            name = l[0]
            ID += 1
            found_ids = set()
            for i in range(1, len(l)):
                if (name, l[i]) in box:
                    found_ids.add(idchecker[(name, l[i])])
            if not found_ids:
                correct = ID
            else:
                correct = min(found_ids)
                for key in idchecker:
                    if idchecker[key] in found_ids:
                        idchecker[key] = correct
            for i in range(1, len(l)):
                box.add((name, l[i]))
                idchecker[(name, l[i])] = correct
        groups = defaultdict(list)
        for (name, email), gid in idchecker.items():
            if not groups[gid]:
                groups[gid].append(name)
            groups[gid].append(email)
        for v in groups.values():
            ans.append([v[0]] + sorted(v[1:]))
        return ans