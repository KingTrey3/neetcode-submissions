class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        i = 0
        while i < len(temperatures):
            counter = 1
            j = i + 1
            while j < len(temperatures):
                if temperatures[i] < temperatures[j]:
                    output[i] = counter
                    break
                else:
                    counter += 1
                    j += 1
            i += 1
        return output
        