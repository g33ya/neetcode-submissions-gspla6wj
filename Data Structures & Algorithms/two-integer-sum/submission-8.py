class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        HashSet or HashMap: Map (finding relationship between elements)
        Key/Value: List element, index
        If-condition: if target - nums[j] in map, return nums[i], j
        '''
        indices = {}

        for j in range(len(nums)):
            if target - nums[j] in indices:
                return [indices[target - nums[j]], j]
            else:
                indices[nums[j]] = j
        