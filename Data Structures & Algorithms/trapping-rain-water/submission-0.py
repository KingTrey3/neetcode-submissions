class Solution:
    def trap(self, height: List[int]) -> int:
        solution = 0
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]

        while left < right:
            if max_left < max_right:
                left += 1
                left_sum = max_left - height[left]
                if left_sum > 0:
                    solution += left_sum
                if height[left] > max_left:
                    max_left = height[left]
            else:
                right -= 1
                right_sum = max_right - height[right]
                if right_sum > 0:
                    solution += right_sum
                if height[right] > max_right:
                    max_right = height[right]
        return solution