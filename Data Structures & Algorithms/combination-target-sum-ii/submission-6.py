class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        candidates.sort()

        def dfs(start, total):

            if total > target:
                return 
            if total == target:
                res.append(subset.copy())
               
                return 
          
            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i-1]:
                    continue

                if total + candidates[i] > target:
                    break 

                subset.append(candidates[i])

                dfs(i + 1, total + candidates[i])

                subset.pop()
        dfs(0, 0 )

        return res