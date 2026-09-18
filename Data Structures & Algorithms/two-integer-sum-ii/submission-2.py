class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ''' 
        create a list to append two index where index 1 must smaller than index 2 

        '''
        right = 0 
        left = len(numbers) - 1

        ans = []
        while right < left:
            plus = numbers[right] + numbers[left]
            if plus == target:
                ans.append(right + 1 )
                ans.append(left + 1)
                return ans
            if plus < target:
                right += 1  
            if  plus > target:
                left -= 1 
            
                

        