class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        def generate(i,lst):
            if i == len(nums):
                ans.add(tuple(lst.copy()))
                return
            generate(i+1,lst)
            lst.append(nums[i])
            generate(i+1,lst)
            lst.pop()
        generate(0,[])
        return list(ans)
    
