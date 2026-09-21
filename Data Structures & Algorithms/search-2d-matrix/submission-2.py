class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        right = len(matrix) - 1
        left = 0 

       

        while left <= right:
            m = (right + left) // 2 

        #First - find the inner list which have target 
        
            # A list which have target
            inner_r = len(matrix[m]) - 1
            inner_l = 0 
            if matrix[m][0] < target and target < matrix[m][len(matrix[m])-1]:
                while inner_l <= inner_r:
                    inner_m = ((inner_r + inner_l // 2))

                    if matrix[m][inner_m] == target:
                        return True
                    elif matrix[m][inner_m] < target:
                        inner_l += 1 
                    else:
                        inner_r -=1
                return False



            elif matrix[m][0] > target:
                    right -=1
            elif matrix[m][len(matrix[m])-1] < target:
                    left += 1 
            else:
                return True 
        return False



            
