import java.util.List;
import java.util.ArrayList;

class Solution {
    List<List<Integer>> ans = new ArrayList<>();
    void traverse(TreeNode root,int n,List<Integer> arr){
        if(root == null) return;
        n -= root.val;
        arr.add(root.val);
        if(root.left == null && root.right == null && n == 0) ans.add(new ArrayList<>(arr));
        traverse(root.left,n,arr);
        traverse(root.right,n,arr);
        arr.remove(arr.size()-1);
    }
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<Integer> arr = new ArrayList<>();
        traverse(root,targetSum,arr);
        return ans;
    }
}