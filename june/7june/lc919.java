class CBTInserter {
    int n = 0;
    TreeNode root;
    int count(TreeNode root){
        if(root == null) return 0;
        return 1 + count(root.left) + count(root.right);
    }
    public CBTInserter(TreeNode root) {
        n = count(root);
        this.root = root;        
    }
    
    public int insert(int val) {
        n += 1;
        String st = Integer.toBinaryString(n);
        int nn = st.length();
        TreeNode nde = root;
        for(int i=1;nn-1>i;i++){
            if(st.charAt(i) == '0') nde = nde.left;
            else nde = nde.right;
        }
        if(st.charAt(nn-1) == '0') nde.left = new TreeNode(val);
        else nde.right = new TreeNode(val);
        return nde.val;
    }
    
    public TreeNode get_root() {
        return root;
    }
}