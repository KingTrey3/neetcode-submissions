class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            for char in word:
                encoded_str += str(ord(char))
                encoded_str += "."
            encoded_str += ","
        return encoded_str        

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        current_word = ""
        current_number = ""
        for char in s:
            if char == ",":
                decoded_list.append(current_word)
                current_word = ""
                continue
            if char == ".":
                current_word += chr(int(current_number))
                current_number = ""
                continue
            current_number += char
        return decoded_list

