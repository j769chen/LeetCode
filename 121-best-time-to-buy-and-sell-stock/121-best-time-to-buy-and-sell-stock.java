class Solution {
    public int maxProfit(int[] prices) {
        int maxVal = 0;
        int minVal = 10001;
        int minValIndex = 0;
        int greatestProfit = 0;
        
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minVal) {
                minVal = prices[i];
                minValIndex = i;
                maxVal = 0;
            }
            
            if (prices[i] > maxVal && i > minValIndex) {
                maxVal = prices[i];
            }
            
            if (maxVal - minVal > greatestProfit) {
                greatestProfit = maxVal - minVal;
            }
        }
        
        return greatestProfit;
        
        
    }
}