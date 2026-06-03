class Solution {
    TreeNode construct(int[] inorder, int[] postorder, int l1, int r1, int l2, int r2) {
        if (l1 > r1) return null;
        int index = l1;
        for (int i = l1; r1 >= i; i++) {
            if (inorder[i] == postorder[r2]) {
                index = i;
                break;    
            }
        }
        int leftSize = index - l1;
        return new TreeNode(postorder[r2],
        construct(inorder, postorder, l1, index - 1, l2, l2 + leftSize - 1),
        construct(inorder, postorder, index + 1, r1, l2 + leftSize, r2 - 1));
    }
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        int r = inorder.length - 1;
        return construct(inorder, postorder, 0, r, 0, r);
    }
}