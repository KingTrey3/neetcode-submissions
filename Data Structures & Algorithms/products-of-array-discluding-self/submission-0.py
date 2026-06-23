class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [0] * len(nums)
        
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    prod *= nums[j]
            answer[i] = prod
        return answer
            
 

        