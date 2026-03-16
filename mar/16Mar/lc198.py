from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        visited = {}
        def traverse(i):
            if i >= len(nums):
                return 0
            if i in visited:
                return visited[i]
            a = traverse(i+2)
            b = traverse(i+3)
            visited[i] = nums[i] + max(a,b)
            return visited[i]
        traverse(0)
        traverse(1)
        return max(visited[0],visited[1])