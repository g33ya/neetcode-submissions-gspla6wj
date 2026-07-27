class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        - dynamic sliding window
        - longest substring: move right once per iteration,
            move left when condition is violated until condition is restored

        without duplicates: use set?
        zxyz
        {z, x, y, z}

        WHEN DO I UPDATE COUNT.
        '''
       
        seen = set()
        longest, count = 0, 0
        l, r = 0, 0

        while r < len(s):
            count += 1
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                count -= 1
         
            longest = max(longest, count)
            seen.add(s[r])
            r += 1

        return longest

       