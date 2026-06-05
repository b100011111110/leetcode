class Solution {
    TreeNode tarverse(int[] nums,int l,int r){
        if(l>r) return null;
        int ind = l;
        for(int i=l;r>=i;i++){
            if(nums[ind] < nums[i]) ind = i;
        }
        return new TreeNode(nums[ind],tarverse(nums,l,ind-1),tarverse(nums,ind+1,r));
    }
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return tarverse(nums,0,nums.length-1);
    }
}