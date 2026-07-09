class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # 1. checking for duplicates
        # 2. need to check the indices i - j (so we'll need a HashMap here)

        duplicates = {}

        for i in range(len(nums)):
            if (nums[i] in duplicates) and (abs(duplicates[nums[i]] - i) <= k):
                return True
            else:
                duplicates[nums[i]] = i
        return False
        
        
