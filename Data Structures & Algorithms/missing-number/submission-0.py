class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        s = sum(range(0, n+1))

        count = 0 

        for i in nums:
            count += i
        print(count)

        if count == s:
            return 0 
        else:
            return (s - count)