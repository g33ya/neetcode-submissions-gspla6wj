class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        - two-pointer approach: swap l/r elements
        """
        l = 0

        for r in range (len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r + 1
            r = r + 1
        return nums 
            

        