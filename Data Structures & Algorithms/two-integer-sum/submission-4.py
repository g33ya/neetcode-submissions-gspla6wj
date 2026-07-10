class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        - Relationship between two data items -> HashMap
        - What should the key/value pair be?
            - Minimum amount of data we can store to solve in one pass
            - key: list element, value: index
            - do subtraction check ( target - j ) to see if i is in map
        '''
        sums = {}
        for i in range(len(nums)):
            if (target - nums[i] in sums):
                return [sums[target - nums[i]], i]
            else:
                sums[nums[i]] = i
        return False
        
        