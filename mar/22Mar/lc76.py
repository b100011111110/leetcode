from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cc = dict(Counter(t))
        st = {}
        have = 0
        need = len(cc)
        j = 0
        ans = ''
        for i in range(len(s)):
            if s[i] in cc:
                st[s[i]] = st.get(s[i], 0) + 1
                if st[s[i]] == cc[s[i]]:
                    have += 1
            while have == need:
                if ans == '' or len(ans) > i - j + 1:
                    ans = s[j:i+1]
                if s[j] in cc:
                    st[s[j]] -= 1
                    if st[s[j]] < cc[s[j]]:
                        have -= 1
                j += 1
        return ans