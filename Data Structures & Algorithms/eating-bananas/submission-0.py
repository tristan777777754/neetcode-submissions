class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ''' 
        k = eat /per hours
        h = u have x hours to eat

        bounday search -> find the bounday left(min) middle right(max) 
        '''
        # so that every piles only spent one hour (maximun)
        #　k = 1, 2, ...... max(pile) <- which only takes u one hour to eat largest amount of bananas, len(piles) hours
        right  = max(piles) 
        #　number of k
        left = 1


        while left < right:
            mid = (left + right)//2
            time = 0
            for i in piles:
                time += math.ceil(i/mid)
            
            if time <= h:
                right = mid 


            elif time > h: 
                left = mid + 1 
        return left 




              
