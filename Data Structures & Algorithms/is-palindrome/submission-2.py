class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        i = 0
        j = len(s) - 1
        while i < j:
            if ord(s[i]) not in range(48, 58) and ord(s[i]) not in range(97, 123):
                i += 1
                continue
            if ord(s[j]) not in range(48, 58) and ord(s[j]) not in range(97, 123):
                j -= 1
                continue
            if ord(s[j]) in range(48, 58) or ord(s[j]) in range(97, 123) and ord(s[i]) in range(48, 58) or ord(s[i]) in range(97, 123):
                if s[j] != s[i]:
                    return False
                else:
                    i += 1
                    j -= 1
        return True    

        