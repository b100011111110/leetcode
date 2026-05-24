import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map = new HashMap<>();
        int[] ans = new int[2];
        ans[0] = ans[1] = -1;
        for(int i=0;nums.length>i;i++){
            Integer n = map.get(target-nums[i]);
            if(n == null){
                map.put(nums[i],i);
            }else{
                ans[0]=n;
                ans[1]=i;
                return ans;
            }
        }
        return ans;
    }
}