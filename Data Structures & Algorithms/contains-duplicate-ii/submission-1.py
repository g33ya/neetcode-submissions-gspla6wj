class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        - relationship between two elements -> HashMap
        - key: list element, value: index
        - loop through the list and add elements to hashmap
        - if we find an element that's already been added:
            - check abs(i - j) <= k
        '''

        duplicates = {}

        for i in range(len(nums)):
            if (nums[i] in duplicates and abs(i - duplicates[nums[i]]) <= k):
                return True
            else:
                duplicates[nums[i]] = i
        return False

