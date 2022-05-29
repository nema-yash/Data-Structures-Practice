class Solution:
    def maxProfit(self, prices: List[int]) -> int:
                
        l = len(prices)
        if l < 2:
            return 0
        
        buy = 0
        sell = 0    
        profit = [0]
    
        for i, p in enumerate(prices):
            if p < prices[buy]:
                buy = i
            elif p > prices[sell] or buy > sell:
                sell = i
                profit.append(prices[sell] - prices[buy])
        
        return max(profit)
            

#Input: prices = [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

#Input: prices = [7,6,4,3,1]
#Output: 0
#Explanation: In this case, no transactions are done and the max profit = 0.