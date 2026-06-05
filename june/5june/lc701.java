class Solution {
    public TreeNode insertIntoBST(TreeNode head, int val) {
        TreeNode temp = new TreeNode(val),nn = head,prev = null;
        while(head != null){
            prev = head;
            if(head.val == val) return nn;
            if(head.val > val) head = head.left;
            else head = head.right;
        }
        if(prev == null) return temp;
        if(prev.val > val) prev.left = temp;
        else prev.right = temp;
        return nn;
    }
}