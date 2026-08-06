class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        F/D: Dynamic
        Pointer jobs: Right explores, left adjusts
        OE/SD: Same direction
        Violation condition: s[r] in seen, will need to move left until not
        Stopping condition: for r in range(len(s))
        '''

        seen = set()
        l = 0
        longest_substring = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1    
            longest_substring = max(r - l + 1, longest_substring)
            seen.add(s[r])
            r += 1
        return longest_substring