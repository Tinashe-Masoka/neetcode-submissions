class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = {}
        answer = 0

        for num in nums :
            if num not in nums_dict :
                nums_dict[num] = [num]
                if num-1 in nums_dict :
                    nums_dict[num-1] += nums_dict[num]
                    nums_dict[num] = nums_dict[num-1]
                    if len(nums_dict[num]) > answer : answer = len(nums_dict[num])
                if num+1 in nums_dict :
                    if len(nums_dict[num+1]) > len(nums_dict[num]) :
                        nums_dict[num+1] += nums_dict[num]
                        nums_dict[num] = nums_dict[num+1]
                    else :
                        nums_dict[num] += nums_dict[num+1]
                        nums_dict[num+1] = nums_dict[num]
                    if len(nums_dict[num]) > answer : answer = len(nums_dict[num])

        if answer == 0 and len(nums) > 0 :
            return 1

        return answer