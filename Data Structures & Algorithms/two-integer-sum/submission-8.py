class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution_dict = {}

        for i in range(len(nums)):
            curr = target - nums[i]
            if curr in solution_dict:
                return [solution_dict[curr], i]
            else:
                solution_dict[nums[i]] = i

        