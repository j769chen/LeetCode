class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = 10001
        maxProfit = 0
        
        for p in prices:
            minP = min(minP, p)
            maxProfit = max(maxProfit, p - minP)
        
        return maxProfit