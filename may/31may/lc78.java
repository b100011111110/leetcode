class Solution {
    List<List<Integer>> ans = new ArrayList<>();
    void traverse(int[] nums,int i,List<Integer> arr){
        if(i==nums.length) return;
        arr.add(nums[i]);
        traverse(nums,i+1,arr);
        if(i == nums.length-1) ans.add(new ArrayList<>(arr));
        arr.remove(arr.size()-1);
        if(i == nums.length-1) ans.add(new ArrayList<>(arr));
        traverse(nums,i+1,arr);
    }
    public List<List<Integer>> subsets(int[] nums) {
        List<Integer> arr = new ArrayList<>();
        traverse(nums,0,arr);
        return ans;
    }
}