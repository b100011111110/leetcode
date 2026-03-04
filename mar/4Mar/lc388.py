class Solution:
    def lengthLongestPath(self, input: str) -> int:
        input = input.split('\n')
        st = []
        ans = 0
        for i in input:
            t = i.count('\t')
            st = st[:t]
            st.append(len(i)-t)
            if '.' in i:
                ans = max(ans,sum(st)+len(st)-1)
        return ans