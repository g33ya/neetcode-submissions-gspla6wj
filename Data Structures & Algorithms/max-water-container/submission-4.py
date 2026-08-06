class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        OE or SD: OE
        Left moves: when heights[l] < heights[r]
        Right moves: when heights[r] < heights[l]
        Stopping condition: !(l < r)
        '''

        max_area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            max_area = max(area, max_area)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area