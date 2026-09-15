class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # same direction or opposite ends
        # OE because we want to maximize l - r
        # we move the pointer with the smaller height
        # find min height, * by difference heights[r] - heights[l]

        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            min_height = min(heights[l], heights[r])
            max_area = max((r-l)* min_height, max_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1
            
        return max_area


            
