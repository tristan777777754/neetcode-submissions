class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []

        #　we can not ues i as parameter in this quesiton 
        # we need to use for loop to avoid to choose the repeat number

        def dfs():
            if len(sub) == len(nums):
                res.append(sub.copy())
                return 

            for num in nums:
                if num in sub:
                    continue
                sub.append(num)

                dfs()

                sub.pop()
        dfs()

        return res
                
     