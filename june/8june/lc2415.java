class Solution {
    public TreeNode reverseOddLevels(TreeNode root) {
        Queue<TreeNode> que = new LinkedList<>();
        que.offer(root);
        boolean isEven = false;
        while(!que.isEmpty()){
            List<TreeNode> arr = new ArrayList<>();
            int n = que.size();
            for(int i =0;n>i;i++){
                TreeNode node = que.poll();
                if(isEven) arr.add(node);
                if(node.left != null)  que.offer(node.left);
                if(node.right != null) que.offer(node.right);
            }
            if(isEven){
                int m = arr.size();
                for(int j =0;m/2>j;j++){
                    int temp = arr.get(j).val;
                    arr.get(j).val = arr.get(m-1-j).val;
                    arr.get(m-1-j).val = temp;
                }
            }
            isEven = !isEven;
        }
        return root;
    }
}