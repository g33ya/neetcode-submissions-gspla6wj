class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        - use two-pointer here
        - left pointer, right pointer, check if equal
            - if yes, l+1 and r-1
                else, return false
        '''

        l = 0
        r = len(s) - 1

        lowercase_s = s.lower()

        while l < r:
            if not lowercase_s[l].isalnum():
                l += 1
                continue
            if not lowercase_s[r].isalnum():
                r -= 1
                continue

            if lowercase_s[l] == lowercase_s[r]:
                l +=1 
                r -=1
            else:
                return False
        return True
        