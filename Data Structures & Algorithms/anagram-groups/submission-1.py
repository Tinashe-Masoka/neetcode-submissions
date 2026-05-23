class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # answer = []
        # str_dict = {}


        # for i in range(len(strs)) :
        #     str_asc = 0

        #     for j in strs[i] :
        #         str_asc += ord(j)
            
        #     if str_asc not in str_dict : 
        #         str_dict[str_asc] = [strs[i]]
        #         continue
            
        #     else : str_dict[str_asc].append(strs[i])

        # for i in str_dict :
        #     answer.append(str_dict[i])

        answer = []
        str_dict = {}

        for i in strs :
            str_tpl = tuple(sorted(i))

            if str_tpl not in str_dict :
                str_dict[str_tpl] = [i]
            else : str_dict[str_tpl].append(i)

        for i in str_dict :
            answer.append(str_dict[i])

            

        return answer


