class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        index

        '''

        charS = defaultdict(list)
        charT = defaultdict(list)

        for i in range(len(s)):
            charS[s[i]].append(i)

        for i in range(len(t)):
            charT[t[i]].append(i)

        # perform a check that the values are equal to each other
        if list(charS.values()) == list(charT.values()):
            return True
        return False