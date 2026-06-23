class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams will have all the same characters
        # 2 hashmaps and compare them

        map_s: dict[str, int] = {}
        map_t: dict[str, int] = {}
        
        for char in s:
            if char in map_s:
                map_s[char] += 1
            else:
                map_s[char] = 1

        for char in t:
            if char in map_t:
                map_t[char] += 1
            else:
                map_t[char] = 1

        return map_s == map_t        
