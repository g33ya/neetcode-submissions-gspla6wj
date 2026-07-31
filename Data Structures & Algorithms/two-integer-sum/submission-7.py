class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
         - Relationship between numbers -> HashMap
         - Key: list element, value: element index
         - 3, 4 target = 7
         - if target - cur num is in map , we've found the other index!
        '''
        numsMap = {}

        for i in range(len(nums)):
            if target - nums[i] in numsMap:
                return [numsMap[target - nums[i]], i]
            else:
                numsMap[nums[i]] = i

        
        