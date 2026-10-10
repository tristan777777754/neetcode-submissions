class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dic = {}
        t_dic = {}

        for i in s:
            if i in s_dic:
                s_dic[i] += 1
            else:
                s_dic[i] = 1 
            
        for j in t:
            if j in t_dic:
                t_dic[j] += 1
            else:
                t_dic[j] = 1
        
        if s_dic == t_dic:
            return True
        else:
            return False
             
