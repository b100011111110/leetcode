class Solution {
    public int deepestLeavesSum(TreeNode root) {
        Queue<TreeNode> que = new LinkedList<>();
        int ans = 0;
        que.offer(root);
        while(!que.isEmpty()){
            int n = que.size(),s = 0;
            for(int i=0;n>i;i++){
                TreeNode nde = que.poll();
                s += nde.val;
                if(nde.left != null) que.offer(nde.left);
                if(nde.right != null) que.offer(nde.right);
            }
            ans = s;
        }
        return ans;
    }
}