class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ''' 
        ith = 1, 2, 3, 4, 5, 6
        '''

        i = 0 
        profit = []
        for i in range(len(prices)):
            
            
            for r in range(i + 1, len(prices)):
                profit.append(prices[r] - prices[i])
       
        print (profit)

        if not profit:
            return 0

        highest_pro = max(profit)

        if highest_pro < 0:
            return 0
        else:
            return highest_pro
