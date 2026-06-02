class Solution {
    double pow(double x,int n){
        if(n == 0) return 1.0;
        if(n == 1) return x;
        double d = pow(x,n/2);
        if(n%2 == 0) return d * d;
        return d * d * x;
    }
    public double myPow(double x, int n) {
        if(n == 0) return 1.0;
        if(n == 1) return x;
        if(0>n){
            x = 1/x;
            n = -1 * n;
        }
        return pow(x,n);
    }
}