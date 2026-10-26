class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = [0] * 26
        l = 0
        max_len = 0
        for r in range(len(s)):
            char_count[ord(s[r]) - ord('A')] += 1
            max_freq = max(char_count)
            total_sum = sum(char_count)
            if total_sum - max_freq > k:
                char_count[ord(s[l]) - ord('A')] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len

        