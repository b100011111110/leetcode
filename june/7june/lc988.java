class Solution {
    String smallest = "~";
    public String smallestFromLeaf(TreeNode root) {
        dfs(root, "");
        return smallest;
    }
    private void dfs(TreeNode node, String current) {
        if (node == null) return;
        current = (char)(node.val + 'a') + current;
        if (node.left == null && node.right == null) {
            if (current.compareTo(smallest) < 0) {
                smallest = current;
            }
            return;
        }
        dfs(node.left, current);
        dfs(node.right, current);
    }
}