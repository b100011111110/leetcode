class Solution {
    public String smallestFromLeaf(TreeNode root) {
        if(root == null) return "";
        char c = (char)(root.val + 'a');
        String l = smallestFromLeaf(root.left) , r = smallestFromLeaf(root.right);
        if(l.equals("")) return r + c;
        if(r.equals("")) return l + c;
        if(l.compareTo(r) > 0) return r + c;
        return l + c;
    }
}