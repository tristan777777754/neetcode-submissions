class Solution:
    def isPalindrome(self, s: str) -> bool:
         
        s = list(s)
        clean_s = []
        for char in s:
            if char.isalnum():
                cahr = char.lower()
                clean_s.append(cahr)
        print(clean_s)


        right = 0
        left = len(clean_s) - 1 
        while right <= left:
            if clean_s[right] == clean_s[left]:
                right += 1
                left -= 1
                continue
            else:
                return False
        return True

