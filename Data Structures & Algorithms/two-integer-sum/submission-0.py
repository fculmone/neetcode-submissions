class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[i] + nums[j] = target
        # target - nums[i] = nums[j]
        value_to_index = {}
        for i, x in enumerate(nums):
            y = target - x 
            if y in value_to_index:
                return sorted([i, value_to_index[y]])
            value_to_index[x] = i