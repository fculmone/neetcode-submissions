class Solution:
    def findMin(self, nums: List[int]) -> int:
        def is_min(i):
            if i == 0:
                return nums[0] <= nums[len(nums) - 1]
            return nums[i] < nums[i - 1]
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(l, mid, r)
            if is_min(mid):
                return nums[mid]
            if nums[mid] >= nums[l] and nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return -9999
        


