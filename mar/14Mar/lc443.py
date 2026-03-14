from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        ans  = 0
        pv = chars[0]
        c = 0
        aa = []
        for i in chars:
            if i == pv:
                c += 1
            else:
                aa.append(pv)
                ans += 1
                if c > 1:
                    aa.extend([i for i in str(c)])
                    ans += len(str(c))
                c = 1
                pv = i
        ans += 1
        aa.append(i)
        if c > 1:
            ans += len(str(c))
            aa.extend([i for i in str(c)])
        for j in range(ans):
            chars[j] = aa[j]
        return ans