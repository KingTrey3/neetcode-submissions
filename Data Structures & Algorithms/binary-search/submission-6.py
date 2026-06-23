class Solution:
    def search(self, nums: List[int], target: int) -> int:
      i: int = 0
      j: int = len(nums) - 1

      while i <= j:
        m: int = (i + j) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
           i = m + 1
        else:
            j = m - 1
      return -1


        