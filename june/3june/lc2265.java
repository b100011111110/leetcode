class Solution {
    int[] traverse(TreeNode root){
        int[] arr = new int[3];
        if(root == null) return arr;
        int[] left = traverse(root.left),right = traverse(root.right);
        arr[0] = root.val + left[0] + right[0];
        arr[1] = 1 + left[1] + right[1];
        arr[2] = left[2] + right[2];
        arr[2] += root.val == (arr[0] /arr[1] )? 1 : 0;
        return arr;
    }
    public int averageOfSubtree(TreeNode root) {
        return traverse(root)[2];
    }
}