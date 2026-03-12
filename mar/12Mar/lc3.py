class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        ans,i,j = 0,0,0
        while len(s)>i:
            if s[i] not in st:
                st.add(s[i])
            else:
                while s[i] in st:
                    st.remove(s[j])
                    j += 1
                st.add(s[i])
            i += 1
            ans = max(ans,i-j)
        return ans