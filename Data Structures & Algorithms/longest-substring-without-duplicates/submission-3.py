class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        left = 0
       
        maxx = 0
        

        for letter in range(len(s)):
           
            # if set {a, b, c} -> 
            while s[letter] in sett :
                sett.remove(s[left])
                left += 1 
            
            sett.add(s[letter])
               
            w_len = (letter - left) + 1
            # print(w_len)
            maxx = max(w_len, maxx)
            
        return maxx



            
