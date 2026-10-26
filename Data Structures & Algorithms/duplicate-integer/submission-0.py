class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for num in nums:
            amount = dups.get(num, 0)
            if amount > 0:
                return True
            dups[num] = 1
        return False    