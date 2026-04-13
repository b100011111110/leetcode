from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1,s2,s3 = set(nums1),set(nums2),set(nums3)
        a1,a2,a3 = s1.intersection(s2),s2.intersection(s3),s3.intersection(s1)
        return list(a1.union(a2).union(a3))