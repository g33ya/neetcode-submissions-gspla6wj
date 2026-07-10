class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        -  to check if we've seen that a value has been seen before, a hashset/map
            can be used
        - do we need a key/value pair, or just a key here?
            - the only data we need is the list element value itself
            - we only need a key -> HashSet
        - the idea: we're going to loop through the list, adding each unique element
            as a key. 
            - if we find a duplicate element, we return true. else, false.
        '''

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

        
    
