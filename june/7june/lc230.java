class Solution {
    int ans = 0,c = 0,kk = 0;
    void traverse(TreeNode root){
        if(root == null) return;
        traverse(root.left);
        c += 1;
        if(c == kk) ans = root.val;
        traverse(root.right);
    }
    public int kthSmallest(TreeNode root, int k) {
        kk=k;
        traverse(root);
        return ans;
    }
}