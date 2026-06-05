class Solution {
    int sum(TreeNode root,boolean parent,boolean grandparent){
        if(root == null) return 0;
        int l = sum(root.left,root.val%2 == 0,parent),r = sum(root.right,root.val%2 == 0,parent);
        if(grandparent) return l + r + root.val;
        return l + r;
    }
    public int sumEvenGrandparent(TreeNode root) {
        return sum(root,false,false);
    }
}