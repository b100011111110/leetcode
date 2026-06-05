class Solution {
    public TreeNode sufficientSubset(TreeNode root, int limit) {
        if(root == null) return null;
        if(root.left == root.right) return root.val < limit ? null : root;
        limit -= root.val;
        root.left = sufficientSubset(root.left,limit);
        root.right = sufficientSubset(root.right,limit);
        return root.left != null || root.right != null ? root : null;
    }
}