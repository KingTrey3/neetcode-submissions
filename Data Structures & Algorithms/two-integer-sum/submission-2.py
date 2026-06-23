class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - list[i] = ?
        # if ? in hash map retern key of hashmap
            # key is the index of array
        # only looping through array once

        prevMap = {} #val : index

        for i, n in enumerate(nums): 
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            

        