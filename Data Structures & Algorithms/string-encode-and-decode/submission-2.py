class Solution:

    def encode(self, strs: List[str]) -> str:
        # use 256 as the delimiter
        def char_to_three_digit_ascii(char: str) -> str:
            num = ord(char)
            if num / 10 < 1:
                return "00" + str(num)
            elif num / 100 < 1:
                return "0" + str(num)
            else:
                return str(num)
            
        
        encoded_str = ""
        for s in strs:
            for char in s:
                encoded_str += char_to_three_digit_ascii(char)
            encoded_str += "256"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        index = 0
        strs = [] 
        curr_str = ""
        while index + 3 < len(s):
            char = s[index:index + 3]
            if char == "256":
                strs.append(curr_str)
                curr_str = ""
            else:
                curr_str += chr(int(char))
            index += 3
        strs.append(curr_str)
        return strs
            