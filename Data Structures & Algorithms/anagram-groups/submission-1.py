class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        1. sorted every charaters in the list
        2. append the word in the inner list
        3. if the charaters already exsit, append that word in that inner list
        '''
     
        # #　sorted 
        # sorted_strs =[]
        # for i in range(len(strs)):
        #     s = sorted((strs[i]))
        #     ss = ''.join(s)
        #     sorted_strs.append(ss)
        #     # print(ss)
        #     # print(sorted_strs)
     

        # print(sorted_strs)

        # # append the word in the inner list
        # # 
        # ans = []
        # for t in  range(len(sorted_strs)):
        #     inner_list = []
        #     if any(strs[t] in j for j in ans):
        #         continue
        #     else:
        #         inner_list.append(strs[t])
            
        #     for i in range(len(sorted_strs)):
        #         if t == i:
        #             continue 
        #         if sorted_strs[t] == sorted_strs[i]:
        #             inner_list.append(strs[i])

        #     ans.append(inner_list)
        #     print(inner_list)
        # return ans

        group = {} # slove this question by using dictionary

        for words in strs:
            key = ''.join(sorted(words))
            if key in group:
                group[key].append(words)
            else:
                group[key] = [words]
 
        ans = []

        for key in group:
            ans.append(group[key])
        return ans

        print(ans)

            



                