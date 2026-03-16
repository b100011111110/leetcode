from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def traverse(i, end):
            if i > end:
                return 0
            if i in visited:
                return visited[i]
            take = nums[i] + traverse(i+2, end)
            skip = traverse(i+1, end)
            visited[i] = max(take, skip)
            return visited[i]
        visited = {}
        first = traverse(0, len(nums)-2)
        visited = {}
        second = traverse(1, len(nums)-1)
        return max(first, second)