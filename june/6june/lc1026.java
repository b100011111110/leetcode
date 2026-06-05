class Solution {
    int d = 0;
    void traverse(TreeNode root,int mi,int mx){
        if(root == null) return;
        if(root.val > mx) mx = root.val;
        if(root.val < mi) mi = root.val;
        if(mx - root.val > d) d = mx - root.val;
        if(root.val - mi > d) d = root.val - mi;
        traverse(root.left,mi,mx);
        traverse(root.right,mi,mx);
    }
    public int maxAncestorDiff(TreeNode root) {
        traverse(root,root.val,root.val);
        return d;
    }
}