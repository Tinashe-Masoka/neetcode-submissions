class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strs_dict = {}

        for word in strs :

            count = [0] * 26

            for char in word :
                count[ord(char) - ord('a')] += 1
            
            count_tpl = tuple(count)

            strs_dict.setdefault(count_tpl,[]).append(word)

        return list(strs_dict.values())

