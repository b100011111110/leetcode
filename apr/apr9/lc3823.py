class Solution:
    def reverseByType(self, s: str) -> str:
        a,b = [],[]
        for i in s:
            if i.isalpha():
                a.append(i)
            else:
                b.append(i)
        st = []
        for i in s:
            if i.isalpha():
                st.append(a.pop())
            else:
                st.append(b.pop())
        return ''.join(st)