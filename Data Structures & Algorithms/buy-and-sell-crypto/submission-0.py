class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        future_max=[0] * n
        sell_max=0
        profit=0

        for i in range(n-1,0,-1):
            sell_max= max( sell_max , prices[i] )
            future_max[i-1] = sell_max
        
        for i in range(n):
            current_profit= future_max[i] - prices[i]
            profit = max( profit , current_profit)

        return profit