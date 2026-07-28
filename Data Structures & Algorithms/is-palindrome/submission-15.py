class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        two pointer opposite ends
        '''
        l, r = 0, len(s) - 1

        s_lower = s.lower()
        while l < r:
            while l < r and not s_lower[l].isalnum():
                l += 1
            while l < r and not s_lower[r].isalnum():
                r -= 1
            
            if s_lower[l] != s_lower[r]:
                print(s_lower[l])
                print(s_lower[r])
                return False
            l += 1
            r -= 1
        return True
