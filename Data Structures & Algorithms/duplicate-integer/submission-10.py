class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        - store list element (no need for index) -> HashSet
        '''
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False