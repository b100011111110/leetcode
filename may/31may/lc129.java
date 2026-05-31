class Solution {
    int ans = 0;
    void traverse(TreeNode root,int n){
        if(root == null) return;
        n *= 10;
        n += root.val;
        if(root.left == null && root.right == null) ans += n;
        traverse(root.left,n);
        traverse(root.right,n);
    }
    public int sumNumbers(TreeNode root) {
        traverse(root,0);
        return ans;
    }
}