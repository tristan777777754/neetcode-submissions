class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest = prices[0]
        maxp = 0
       


        for i in prices:
            profit = i - lowest

            if profit > maxp:
                maxp = profit
            
            if i < lowest:
                lowest = i
        
        
        if maxp < 0:
            return 0
        else:
            return maxp

            

