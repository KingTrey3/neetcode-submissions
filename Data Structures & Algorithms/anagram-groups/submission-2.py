class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution_list = []
        solution_map_list = []

        for word in strs:
            new_map = {}
            for i in range(len(word)):
                char = word[i]
                if char in new_map:
                    new_map[char] += 1
                else:
                    new_map[char] = 1
            index = 0
            if new_map not in solution_map_list:
                solution_map_list.append(new_map)
                solution_list.append([word])
            else:
                for index in range(len(solution_map_list)):
                    if new_map == solution_map_list[index]:
                        # put the word in the proper list
                        solution_list[index].append(word)
                        break
            
        
        return solution_list


        