class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer = []

        pointer_1 = 0
        pointer_2 = len(numbers) - 1

        while pointer_1 < pointer_2:
            num_sum = numbers[pointer_1] + numbers[pointer_2]
            if num_sum == target:
                return [pointer_1 + 1, pointer_2 + 1]
            if num_sum > target:
                pointer_2 -= 1
            else:
                pointer_1 += 1
            
        