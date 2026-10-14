class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_price = prices[0]

        for i in range(len(prices)):

            # 1. 更新 min_price
            if prices[i] < min_price:
                min_price = prices[i]

            # 2. 計算今天賣出的 profit
            profit = prices[i] - min_price

            # 3. 更新 max_profit

            max_profit = max(max_profit, profit)

        return max_profit

        
        


