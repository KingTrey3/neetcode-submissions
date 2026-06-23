class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency_map = {}
        for num in nums:
            if num in frequency_map:
                return True
            else:
                frequency_map[num] = num
        return False
