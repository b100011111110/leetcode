class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0] 
        for i in s:
            if i == "(":
                st.append(0)
            else:
                lc = st.pop() 
                st[-1] += max(1,lc*2)
        return st[-1]