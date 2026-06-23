class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        solution_map = {}

        i = 0

        while i < len(nums):
            sum_num = target - nums[i]
            if sum_num in solution_map:
                    return [solution_map[sum_num], i]
            solution_map[nums[i]] = i   
            i += 1
        