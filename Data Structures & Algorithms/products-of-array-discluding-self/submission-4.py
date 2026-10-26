class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1 
        contains_zero = False
        for n in nums:
            if n != 0:
                total_product *= n
            elif n == 0 and contains_zero:
                total_product = 0
            else:
                contains_zero = True


        retval = []
        for i in range(len(nums)):
            if nums[i] == 0:
                retval.append(total_product) 
            elif contains_zero:
                retval.append(0)
            else:
                retval.append(total_product // nums[i])
        return retval
        