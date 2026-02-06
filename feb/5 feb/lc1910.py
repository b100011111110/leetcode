class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st = ''
        m = len(part)
        for i in s:
            st += i
            if st[-m:] == part:
                st = st[:-m]
        return st