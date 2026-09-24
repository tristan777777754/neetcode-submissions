class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        '''
        think about left, rgiht as boundary and size of window
        '''

        left = 0
        maxx = 0

        
        # count the number of the letter appeared
        count = {}

        
        
        for r in range(len(s)):
           
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            

           
            # why we need to use while loop to shrink not if, because 
            # -> everytime we shrunk s[left] doesnt mean that it is the letter 
            # which we want to remove
            while ((r - left ) + 1) - max(count.values()) > k:
                
                count[s[left]] -= 1
                left += 1 

            window = (r - left ) + 1

            maxx = max(maxx, window)

        return maxx




            

        

                    
                    
