class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        | Submission: 0 |
        
        Have I seen this value before? -> HashSet
        """

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        

