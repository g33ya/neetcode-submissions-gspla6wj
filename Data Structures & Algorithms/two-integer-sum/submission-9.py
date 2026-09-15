class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} 

        for i in range(len(nums)):
            target_dif = target - nums[i]
            if target_dif in indices:
                return [indices[target_dif], i]
            else:
                indices[nums[i]] = i        