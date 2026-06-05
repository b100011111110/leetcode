class Solution {
    public boolean isEvenOddTree(TreeNode root) {
        Queue<TreeNode> que = new LinkedList<>();
        que.offer(root);
        boolean isEven = false;
        while(!que.isEmpty()){
            int n = que.size(),prev = 0;
            if(isEven) prev = Integer.MAX_VALUE;
            else prev = Integer.MIN_VALUE;
            for(int i =0;n>i;i++){
                TreeNode node = que.poll();
                if(isEven){
                    if (node.val >= prev || node.val %2 != 0) return false;
                }else{
                    if(node.val <= prev || node.val %2 == 0) return false;
                }
                if(node.left != null) que.offer(node.left);
                if(node.right != null) que.offer(node.right);
                prev = node.val;
            }
            isEven = !isEven;
        }
        return true;
    }
}