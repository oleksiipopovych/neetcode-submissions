class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start = 0
        for i in range (1, len(prices)):
            if (prices[start] > prices[i]):
                start = i
            profit = max(profit, prices[i] - prices[start])
        
        return profit
        