class Solution:
    def search(self, nums: List[int], target: int) -> int:

        right = len(nums) - 1 

      
        left = 0


        while left  <= right :
            m = (right + left)//2
            print(m)
      
            if nums[m] == target:
                return m 
            elif nums[m] < target:
                left += 1
            else:
                right -= 1
        return -1 


 