class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_dict = {} #model { num : count }
        count_dict = {} #model { count : {num set} }
        answer_list = []
        highest_count = 0

        for num in nums :
            nums_dict[num] = nums_dict.get(num,0) + 1

            if nums_dict[num] > highest_count :
                highest_count = nums_dict[num] 
        

        for num in nums_dict :
            count_dict.setdefault(nums_dict[num],set()).add(num)
        
        while len(answer_list) != k :
            if highest_count in count_dict :
                answer_list += list(count_dict[highest_count])
                
            highest_count -= 1

        return answer_list
            
            




