class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_dict = {} #model { num : count }
        answer_list = []
        highest_count = 0

        for num in nums :
            nums_dict[num] = nums_dict.get(num,0) + 1

            if nums_dict[num] > highest_count :
                highest_count = nums_dict[num] 

        buckets = [[] for _ in range(highest_count + 1)]
        
        for num, count in nums_dict.items() :
            buckets[count].append(num)

        while len(answer_list) < k :
            answer_list += buckets[highest_count]
            highest_count -= 1

        return answer_list

            
            




