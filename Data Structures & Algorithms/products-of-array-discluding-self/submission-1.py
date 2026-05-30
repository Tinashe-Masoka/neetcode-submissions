class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        one_zero = False
        two_zero = False
        total_product = 1
        nums_dict = {}
        answer =[]

        for i in range(len(nums)) :
            nums_dict[nums[i]] = nums_dict.get(nums[i],0) + 1
            if nums[i] == 0 :
                if nums_dict[0] > 1 :
                    two_zero = True
                one_zero = True
                continue
            total_product *= nums[i]
        
        if two_zero :
            return [0 for _ in range(len(nums))]

        if one_zero :
            for num in nums :
                if num == 0 : 
                    answer.append(total_product)
                    continue
                answer.append(0)
            return answer

        return [int(total_product*(num**-1)) for num in nums]
        


        
            


            