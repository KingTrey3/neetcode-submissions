class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_dict = {}

        i = 0

        while i < len(nums):
            diff = target - nums[i]
            if diff in my_dict:
                return [my_dict[diff], i]
            my_dict[nums[i]] = i
            i += 1    