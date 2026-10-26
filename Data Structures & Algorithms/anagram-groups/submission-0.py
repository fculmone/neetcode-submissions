class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(n * m) prolly not right
        # returns a list of a dictionary that counts each letter
        def get_char_counts(strs: List[str]) -> List[Dict[str, int]]:
            retval = []
            for s in strs:
                char_count = {}
                for c in s:
                    char_count[c] = char_count.get(c, 0) + 1
                retval.append(char_count)                                          
            return retval
        
        grouped_anagrams = []
        char_counts = get_char_counts(strs)

        # O(n)
        def str_to_tuple(s: str) -> Tuple[str]:
            letter_count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                letter_count[index] += 1
            return tuple(letter_count)

        """
        The plan
        could group them based on number of letter counts i don't see any other way
        if you do this using an array of 26 indices, we technically get o(m) space since it's one per string

        I could hash the list if I convert it into a tuple
        """
        groups = {}
        for s in strs:
            char_count = str_to_tuple(s)
            if char_count in groups:
                groups[char_count].append(s)
            else:
                groups[char_count] = [s] 
        retval = []
        for value in groups.values():
            retval.append(value)
        return retval