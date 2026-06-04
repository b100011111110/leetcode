class TreeNode {
    int val;
    TreeNode left,right;
}

class Solution {
    public String tree2str(TreeNode root) {
        if(root == null) return "";
        if(root.left == null && root.right == null) return ""+root.val;
        String l = tree2str(root.left),r = tree2str(root.right);
        String arr = "" + root.val;
        if(!r.equals("")) r = "(" + r + ")";
        if(l.equals("")){
            if(!r.equals("")) l = "()";
        }else l = "(" + l + ")";
        return arr + l + r;
    }
}