from typing import *

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st,p = [],len(temperatures)
        ans = [0] * p
        for i in range(1,len(temperatures)+1):
            while st and temperatures[st[-1]-1] <= temperatures[-i]:
                st.pop()
            ans[p-1],p = st[-1]-p if st != [] else 0,p-1
            st.append(p+1)
        return ans