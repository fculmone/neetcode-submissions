class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        retval = []
        retval_set = set()
        i = 0
        while i < len(nums):
            target = nums[i] * -1
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    vals = sorted([nums[i], nums[l], nums[r]])
                    if tuple(vals) not in retval_set:
                        retval.append(vals)
                        retval_set.add(tuple(vals))
                    l += 1
                    r -= 1
                elif target > nums[l] + nums[r]:
                    l += 1
                else:
                    r -= 1;
            i += 1

        return retval 