class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
         # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
        #nvm build the set first then only go through the sets, that way we avoi the
        # O(n^2) runtime that we would have if we checked the set as we build it
        for n in nums:
            nums_set.add(n)
        
        longest_seq = 0
        if len(nums) > 0:
            longest_seq = 1
        for n in nums_set:
            if n + 1 in nums_set and n - 1 not in nums_set:
                curr = n
                curr_len = 0
                while curr in nums_set:
                    curr_len += 1
                    curr += 1
                longest_seq = max(longest_seq, curr_len) 

        return longest_seq