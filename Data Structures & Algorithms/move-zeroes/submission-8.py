class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        want all non-zero values to swap to the right !
        two-pointers same direction:
        movement rule: right pointer should move until landing on nonzero,
        if l != 0 then swap with left pointer
        """
       
        l, r = 0, 1

        while r < len(nums):
            while r < len(nums) - 1 and nums[r] == 0:
                r += 1
            
            while l < r and nums[l] != 0:
                l += 1
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
       
        return nums


        