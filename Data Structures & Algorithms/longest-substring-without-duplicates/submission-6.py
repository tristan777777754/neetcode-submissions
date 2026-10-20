class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0 

        sett = set()

        for r in range(len(s)):
            

            while s[r] in sett:
                sett.remove(s[l])
                l += 1 
            
            sett.add(s[r])
            length = r - l + 1

            max_len = max(length, max_len)
        return max_len





