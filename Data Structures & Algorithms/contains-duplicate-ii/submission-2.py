class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        hashmap
        key = list element, value = element index
        if num in map and abs(i - j) <= k, return true
        '''
        
        numsMap = {}

        for i in range(len(nums)):
            if nums[i] in numsMap and abs(numsMap[nums[i]] - i) <= k:
                return True
            else:
                numsMap[nums[i]] = i
        return False