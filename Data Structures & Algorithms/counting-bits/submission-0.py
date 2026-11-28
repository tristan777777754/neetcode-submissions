class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n+1):
            b = bin(i)
            count = 0

            for j in b:
                if j == "1":
                    count += 1
            ans.append(count )

        return ans   

        