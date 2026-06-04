import java.util.*;

class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        Queue<Node> que = new LinkedList<>();
        List<List<Integer>> ans = new ArrayList<>();
        que.offer(root);
        while(!que.isEmpty()){
            ArrayList<Integer> arr = new ArrayList<>();
            int n = que.size();
            for(int i=0;n>i;i++){
                Node nde = que.poll();
                arr.add(nde.val);
                que.addAll(nde.children);
            }
            ans.add(arr);
        }
        return ans;
    }
}