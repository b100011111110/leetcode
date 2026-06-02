class Solution {
    public int maxProfit(int[] prices) {
        int s = 0;
        for(int i=0;prices.length-1>i;i++){
            if(prices[i+1]-prices[i] > 0) s += prices[i+1]-prices[i];
        }
        return s;
    }
}