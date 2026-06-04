class TreeNode {
    int val;
    TreeNode left,right;
}

class Solution {
    int n = 0;
    public TreeNode convertBST(TreeNode root) {
        if(root == null) return null;
        convertBST(root.right);
        n += root.val;
        root.val = n;
        convertBST(root.left);
        return root;
    }
}