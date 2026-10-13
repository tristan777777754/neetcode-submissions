class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        # print(s)
        
        clean = []
        for i in s:
            if i.isalnum():
                lower = i.lower()
                clean.append(lower)
        print(clean)

        left = 0 
        right = len(clean) - 1

        while left <= right:
            if clean[left] == clean[right]:
                left += 1
                right -=1
            else:
                return False
        return True



