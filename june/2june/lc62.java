class Solution {
    public int uniquePaths(int m, int n) {
        int[][] arr = new int[m][n];
        arr[0][0] = 1;
        for(int i=0;m>i;i++){
            for(int j = 0;n>j;j++){
                int a = 0;
                if(i != 0) a = arr[i-1][j];
                if(j != 0) a += arr[i][j-1];
                if(i == 0 && j == 0) a = 1;
                arr[i][j] = a;
            }
        }
        return arr[m-1][n-1];
    }
}