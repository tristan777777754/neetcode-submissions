class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1 
        

        while left <= right:
            
            mid =(right + left)//2

            # print(matrix[mid][-1])

            if matrix[mid][0] > target :
                right = mid  - 1

            elif matrix[mid][0] <= target and matrix[mid][-1] >= target:
                inner_l = 0
                inner_r = len(matrix[mid]) - 1

                while inner_l <= inner_r:
                    inner_mid = (inner_l + inner_r)//2
                    if matrix[mid][inner_mid] < target:
                        inner_l = inner_mid + 1
                    elif  matrix[mid][inner_mid] > target:
                        inner_r = inner_mid -1 
                    else:
                        return True
                return False
           
            else:
                left = mid + 1
        return False
     



