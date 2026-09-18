class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for number in nums:
            if number in dic:
                dic[number] += 1
            else:
                dic[number] = 1
        #　current dic = {1: 1, 2: 2, 3: 3}
        ans = []
        for i in range(k): # USE MAX TO FIND THE MAXIMUN NUMBER
            max_k = max(dic, key = dic.get)
            del dic[max_k] #delete the max key in dic, so we can get second number 
            ans.append(max_k)
        return ans
        print(ans)
