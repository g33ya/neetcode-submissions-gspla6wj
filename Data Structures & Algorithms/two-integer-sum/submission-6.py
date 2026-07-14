class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        - relationship between elements -> HashMap
        - key: list element, value: index
        - 3 + ? = 7  -> target - nums[j] = nums[i] -> check if nums[i] exists in map
        '''

        indices = {}

        for i in range(len(nums)):
            if (target - nums[i] in indices):
                return [indices[target - nums[i]], i]
            else:
                indices[nums[i]] = i