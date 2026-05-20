class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = -1
        buy = prices[0]
        sell = prices[0]
        for i, n in enumerate(prices):
            if i == 0:
                continue
            
            buy = min(buy, prices[i-1])
            sell = prices[i]

            profit =  max(sell-buy, profit)

        print(profit)

        if profit < 0:
            return 0
        return profit