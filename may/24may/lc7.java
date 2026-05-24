class Solution {
    public int reverse(int x) {
        int s = x > 0 ? 1 : -1;
        x *= s;
        long c = 0;
        while(x != 0){
            c = c*10 + x%10;
            x /= 10;
        }
        if(c > Integer.MAX_VALUE || c<Integer.MIN_VALUE) return 0;
        return (int)c*s;
    }
}