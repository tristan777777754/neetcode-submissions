class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        
        
        #j is not equal to i
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i == j: # the position of i and j can not be the same
                    continue
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans
                else:
                    j += 1  