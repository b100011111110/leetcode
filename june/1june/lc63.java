class Solution {
    public int uniquePathsWithObstacles(int[][] grid) {
        int n = grid.length,m=grid[0].length;
        int[][] path = new int[n][m];
        for(int i=0;n>i;i++){
            for(int j=0;m>j;j++){
                int c = 0;
                if(grid[i][j] == 1) continue;
                if(i == 0 && j == 0) c = 1;
                if(i != 0) c = path[i-1][j];
                if(j != 0) c += path[i][j-1];
                path[i][j] = c;
            }
        }
        return path[n-1][m-1];
    }
}