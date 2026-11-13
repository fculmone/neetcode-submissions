class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # plan is to turn each string into a tuple of 26 positions
        # then put these in a dictionary using the tuple as a key then iterate over the values
        # key is tuple, val is list of strings
        char_count_to_str = {}
        for s in strs:
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - ord('a')] += 1
            char_count = tuple(char_count)
            if char_count in char_count_to_str.keys():
                char_count_to_str[char_count].append(s)
            else:
                char_count_to_str[char_count] = [s]
            
        return list(char_count_to_str.values())

