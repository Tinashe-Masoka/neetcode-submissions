class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        num1 = 0
        num2 = 1

        while num1 < len(numbers) :
            need = target - numbers[num1]

            while numbers[num2] < need and num2 < len(numbers) - 1 :
                num2 += 1
            
            if numbers[num1] + numbers[num2] == target :
                return [ num1+1 , num2+1 ]
            
            num1 += 1
            num2 = num1 + 1
        

            

