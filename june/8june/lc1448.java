class Solution {
    int n = 0;
    void count(TreeNode root,int mx){
        if(root == null) return ;
        if(root.val > mx) mx = root.val;
        else n++;
        count(root.left,mx);
        count(root.right,mx);
    }
    public int goodNodes(TreeNode root) {
        count(root,root.val);
        return n;
    }
}