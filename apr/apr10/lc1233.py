from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        st = set()
        for i in folder:
            x = i.split('/')
            fol = ''
            for j in x[1:]:
                fol += '/' + j
                if fol in st:
                    break
            else:
                st.add(i)
        return list(st) 