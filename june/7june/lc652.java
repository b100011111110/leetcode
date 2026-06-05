class Solution {
    Map<String,TreeNode> map = new HashMap<>();
    Set<String> set = new HashSet<>();
    String traverse(TreeNode root){
        if(root == null) return "#";
        String l = traverse(root.left) , r = traverse(root.right);
        String c = "(" + root.val + "," + l + "," + r + ')';
        if(set.contains(c) && map.getOrDefault(r,null) == null) map.put(c,root);
        set.add(c);
        traverse(root.left);
        traverse(root.right);
        return c;
    }
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        traverse(root);
        return new ArrayList<>(map.values());
    }
}