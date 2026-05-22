class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_dict = {}

        for i in range(len(nums)):

            if nums[i] not in nums_dict : nums_dict[nums[i]] = i
            else:
                if nums[i] * 2 == target : return [nums_dict[nums[i]],i]


            if target - nums[i] in nums_dict and nums_dict[target - nums[i]] != i:
                return [nums_dict[target - nums[i]], i]