class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        res = 0 

        for i in range(0, n+1):
            res = res ^ i 

        for j in nums:
            res = res ^ j 

        return res