class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        - need to track both index and value -> HashMap
        - key: list element, value: index
        - will need to check both contraints (duplicates and abs(i-j) <= k)
        '''

        numsMap = {}

        for i in range(len(nums)):
            if (nums[i] in numsMap) and (abs(numsMap[nums[i]] - i) <= k):
                return True
            else:
                numsMap[nums[i]] = i
        return False
        