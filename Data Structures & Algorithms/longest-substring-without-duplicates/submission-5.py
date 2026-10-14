class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0 
        lenth = 0 
        sett = set()

        for right in range(len(s)):

            while s[right] in sett: #[abc] b -> remove a, b -> [c, b] 
                sett.remove(s[left])
                left+= 1 
            sett.add(s[right])
            inner_lenth = (right - left) + 1 

            lenth = max(inner_lenth, lenth)
        return lenth 

      