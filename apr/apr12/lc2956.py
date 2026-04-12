from collections import Counter
from typing import List, Tuple

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a,b = Counter(nums1),Counter(nums2)
        x,y = 0,0
        for i in a:
            x += a[i] if b[i] else 0
        for i in b:
            y += b[i] if a[i] else 0
        return [x,y]