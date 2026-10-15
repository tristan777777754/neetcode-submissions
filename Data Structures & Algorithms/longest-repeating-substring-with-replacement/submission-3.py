class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0

        max_l = 0

        count = {} # count the number of the letter

        for right in range(len(s)):

            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1 
                left +=1
            
            max_l = max((right - left + 1), max_l)
        return max_l
            
            

            

