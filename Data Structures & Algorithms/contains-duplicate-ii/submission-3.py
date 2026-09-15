class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}

        for i in range(len(nums)):
            if nums[i] in indices and abs(indices[nums[i]] - i) <= k:
                return True
            else:
                indices[nums[i]] = i
        return False