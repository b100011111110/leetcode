class Solution {
    public int minPathSum(int[][] grid) {
        int n=grid.length,a=grid[0].length;
        int[][] path = new int[n][a];
        for(int i=0;n>i;i++){
            for(int j=0;a>j;j++){
                path[i][j] = grid[i][j];
                int m = 0;
                if(i != 0) m = path[i-1][j];
                if(j != 0) {
                    if(m == 0) m = path[i][j-1];
                    else if(path[i][j-1] < m) m = path[i][j-1];
                }
                path[i][j] += m;
            }
        }
        return path[n-1][a-1];
    }
}