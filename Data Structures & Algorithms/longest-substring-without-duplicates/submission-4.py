class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        - dynamic sliding window
        - longest substring: move right once per iteration,
            move left when condition is violated until condition is restored
        '''

        seen = set()

        l, r = 0, 0
        longest_length = 0

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[l])
            
            seen.add(s[r])
            longest_length = max(longest_length, r - l + 1)
            r += 1
        return longest_length