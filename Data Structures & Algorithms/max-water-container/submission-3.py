class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        tracking two bars -> two pointers
        opposite ends or same direction?

        max amount = area = r - l * max(height l, height r)
        let's try opposite ends first..
        '''

        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            curr_area = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, curr_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area