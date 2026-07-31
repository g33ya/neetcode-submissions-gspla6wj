class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        two-pointers. opposite ends
        movement rule: if s[l] == s[r], l+=1 and r-=1
                       if s[l] != s[r], then check if substring reversed is
                       equal
        can either "remove" the left value or right value
        '''
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
            else:
                left_removed = s[l + 1:r + 1]
                right_removed = s[l:r]
                return left_removed == left_removed[::-1] or right_removed == right_removed[::-1]
        return True