import java.util.*;

class Solution {
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        Queue<TreeNode> que = new LinkedList<>();
        if(root == null) return ans;
        que.offer(root);
        while(!que.isEmpty()){
            int n = que.size(),mx = 0;
            for(int i=0;n>i;i++){
                TreeNode nde = que.poll();
                if(nde.val > mx) mx = nde.val;
                if(nde.left != null) que.offer(nde.left);
                if(nde.right != null) que.offer(nde.right);
            }
            ans.add(mx);
        }
        return ans;
    }
}