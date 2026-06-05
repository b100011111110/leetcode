class Solution {
    public int findBottomLeftValue(TreeNode root) {
        Queue<TreeNode> que = new LinkedList<>();
        que.offer(root);
        int ans = 0;
        while(!que.isEmpty()){
            int n = que.size();
            ans = que.peek().val;
            for(int i=0;n>i;i++){
                TreeNode nde = que.poll();
                if(nde.left != null) que.offer(nde.left);
                if(nde.right != null) que.offer(nde.right);
            }
        }
        return ans;
    }
}