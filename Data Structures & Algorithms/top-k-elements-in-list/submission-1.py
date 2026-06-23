class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        solution_list = [None] * k 
        freq_map = {}

        for num in nums: 
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        for index in range(k):
            max_value = -999
            for key in freq_map:
                if freq_map[key] > max_value:
                    solution_list[index] = key
                    max_value = freq_map[key]
            freq_map.pop(solution_list[index])
        
        return solution_list
        