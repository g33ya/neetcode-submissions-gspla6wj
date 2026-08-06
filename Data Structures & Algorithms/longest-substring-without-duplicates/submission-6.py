class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        sliding window: dynamic
        - move pointers until condition is no longer violated

        what are my conditions here?
        - we can use a set to track characters we've seen
        - if a character we see is in the set, violation!
        - move the right pointer (traverse). at violation, move left (fix).
        '''
        
        seen = set()
        max_len = 0
        l = 0

        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            
            seen.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len
