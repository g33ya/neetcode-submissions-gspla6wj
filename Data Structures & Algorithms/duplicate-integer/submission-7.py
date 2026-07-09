class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Checking if we've seen a value before -> HashSet (just a key)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
