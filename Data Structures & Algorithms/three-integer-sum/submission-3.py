class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        #　becauee i+j+k = 0, hence i = k - j 
        # how to get i ?　
        i = 0 
        k = 1
        j = len(nums) - 1 
        
        ans = []

        while i < len(nums):
            
            k = 1 + i
            j = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            



            while k < j:
            
                target = -nums[i] 
                group = []
                if nums[k] + nums[j] == target:
                    group.append(nums[k])
                    group.append(nums[j])
                    group.append(nums[i])
                    ans.append(group)
                    k += 1 
                    j -= 1 
                    print(group)
                    while k < j and nums[k] == nums[k - 1]:
                        k += 1

                    while k < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif nums[k] + nums[j] < target:
                    k += 1 

                else: 
                    j -= 1 
                
                
            i += 1
   
        return ans

          
            
           
       