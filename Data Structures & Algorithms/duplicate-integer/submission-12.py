class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        duplicate = hashing
        set or map? -> just need key -> set
        O(n)
        '''
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        
        
    
