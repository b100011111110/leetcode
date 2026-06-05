class Solution {
    public int maxLevelSum(TreeNode root) {
        Queue<TreeNode> que = new LinkedList<>();
        int ans = Integer.MIN_VALUE,l = 0,al = 0;
        que.offer(root);
        while(!que.isEmpty()){
            l++;
            int n = que.size(),s = 0;
            for(int i=0;n>i;i++){
                TreeNode nde = que.poll();
                s += nde.val;
                if(nde.left != null) que.offer(nde.left);
                if(nde.right != null) que.offer(nde.right);
            }
            if(ans < s) {
                ans = s;
                al = l;
            }
        }
        return al;
    }
}