class Solution {
    TreeNode construct(int[] preorder, int[] inorder,int l1,int r1,int l2,int r2){
        if(l1>r1) return null;
        int index = l2;
        for(int i=l2;r2>=i;i++){
            if(inorder[i] == preorder[l1]) {
                index = i;
                break;    
            }
        }
        int leftSize = index - l2;
        return new TreeNode(preorder[l1],
        construct(preorder, inorder, l1 + 1, l1 + leftSize, l2, index - 1),
        construct(preorder, inorder, l1 + leftSize + 1, r1, index + 1, r2));
    }
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int l=0,r=inorder.length-1;
        return construct(preorder,inorder,0,r,0,r);
    }
}