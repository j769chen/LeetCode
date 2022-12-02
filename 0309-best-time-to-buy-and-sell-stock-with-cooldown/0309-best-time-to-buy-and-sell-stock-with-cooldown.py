class Solution:
    # we keep track of the current state, i.e. we can only do certain operations based on what 
    # the previous operation was, and get the amount of money that we make going down each 
    # decision tree and cache it. If we encounter the same i and buying pair, we can just 
    # reference the hashmap, eventually, we return the max profit for the entire tree
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2
        
        dp = {} # key=(i, buying) val=max_profit
        
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i+1, buying)
            
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
                
            return dp[(i, buying)]
        
        return dfs(0, True)