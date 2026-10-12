class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = {}

        for key in strs:
            s_key = "".join(sorted(key))
            if s_key in dic:
                dic[s_key].append(key)
            else:
                dic[s_key] = [key]
        # print(dic)
        
        ans = []

        for key in dic:
            ans.append(dic[key])
        # print(ans)
        return ans

        
       
            
        

    
            