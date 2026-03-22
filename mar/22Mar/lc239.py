from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        ans = []
        for i in range(len(nums)):
            while que and que[-1] < nums[i]:
                que.pop()            
            que.append(nums[i])
            if i >= k and que[0] == nums[i - k]:
                que.popleft()
            if i >= k - 1:
                ans.append(que[0])  
        return ans