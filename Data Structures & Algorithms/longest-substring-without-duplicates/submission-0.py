class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        chars_set = set()
        l = 0
        for r in range(len(s)):
            while s[r] in chars_set:
                chars_set.remove(s[l])
                l += 1
            chars_set.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len
        