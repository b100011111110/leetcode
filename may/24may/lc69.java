class Solution {
    public int mySqrt(int x) {
        long l=0,r=x;
        while(r>=l){
            long m = l + (r-l)/2 ;
            if(m*m == x) return (int)m;
            if(m*m > x){
                r = m-1;
            }else{
                l = m+1;
            }
        }
        return (int)r;
    }
}