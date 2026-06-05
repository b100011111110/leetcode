class Solution {
    TreeNode traverse(TreeNode root,int val,int depth){
        if(root == null) return null;
        if(depth == 2){
            TreeNode l = new TreeNode(val,root.left,null),r = new TreeNode(val,null,root.right);
            root.left = l;
            root.right = r;
            return root;
        }
        traverse(root.left,val,depth -1);
        traverse(root.right,val,depth -1);
        return root;
    }
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if(depth == 1) return new TreeNode(val,root,null);
        return traverse(root,val,depth);
    }
}