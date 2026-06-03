class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        TreeNode prev = null,temp = root,left,right,nleft;
        while(root != null && root.val != key){
            prev = root;
            if(root.val > key) root = root.left;
            else root = root.right;
        }
        if(root == null) return temp;
        if(prev != null && root.left == null){
            if(prev.left != null && prev.left.val == key) prev.left = root.right;
            else prev.right = root.right;
            return temp;
        }
        left = nleft = root.left;
        right = root.right;
        while(nleft != null && nleft.right != null) nleft = nleft.right;
        if(nleft != null) nleft.right = right;
        if(prev == null) return left == null ? right: left;
        if(prev.left != null && prev.left.val == key) prev.left = left;
        else prev.right = left;
        return temp;
    }
}