from typing import *

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in asteroids:
            if st == []:
                st.append(i)
            elif i > 0:
                st.append(i)
            elif i < 0 and st[-1] < 0:
                st.append(i)
            elif st[-1] > 0 and i < 0:
                while st != [] and st[-1] > 0 and abs(i) > st[-1]:
                    st.pop()
                if st == []:
                    st.append(i)
                elif st[-1] + i == 0:
                    st.pop()
                elif st[-1] < 0 and i < 0:
                    st.append(i)
        return st