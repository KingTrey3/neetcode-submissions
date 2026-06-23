class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a hash map
        # if duplicate return true if not false

        my_map: dict[int, int] = {}

        for number in nums:
            if number in my_map:
                return True
            else:
                my_map[number] = number
        return False
         