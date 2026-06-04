import java.util.*;

class TreeNode {
    int val;
    TreeNode left,right;
}

class Solution {
    Map<Integer,Integer> map = new HashMap<>();
    int traverse(TreeNode root){
        if(root == null) return 0;
        int l = traverse(root.left),r = traverse(root.right);
        int s = root.val + l + r;
        map.put(s,map.getOrDefault(s,0)+1);
        return s;
    }
    public int[] findFrequentTreeSum(TreeNode root) {
        traverse(root);
        int f = 0;
        for (Map.Entry<Integer,Integer> entry : map.entrySet()) {
            if(f < entry.getValue()) f = entry.getValue();
        }
        ArrayList<Integer> arr = new ArrayList<>();
        for (Map.Entry<Integer,Integer> entry : map.entrySet()) {
            if(f == entry.getValue()) arr.add(entry.getKey());
        }
        return arr.stream().mapToInt(i -> i).toArray();    
    }
}