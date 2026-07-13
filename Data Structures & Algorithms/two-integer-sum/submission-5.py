class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        - finding relationship between two list elements -> hashmap
        - key: list element, value: index (minimum amount of data to solve in one pass)
        - [3,4,5,6], target = 7 | 3 + 4 = 7 
        - check: target - list element is IN hashmap -> if so, we found the other element
        '''

        sums = {}

        for i in range(len(nums)):
            if (target - nums[i] in sums):
                return [sums[target - nums[i]], i]
            else:
                sums[nums[i]] = i