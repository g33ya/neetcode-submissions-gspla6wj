class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        will need to do multipication
        - biggest difference in index paired with the highest list element
        - (highest list element - height of the lower index w/ biggest difference)
        - 

        two pointer (opposite end)
        store the areas in a list
        return the max area from that list at the end
        '''

        l, r = 0, len(heights) - 1


        # difference in index * min(two heights)
        max = 0
        while l < r:
            

            if ((r - l) * min(heights[l], heights[r]) > max):
                max = (r - l) * min(heights[l], heights[r])

            if (heights[l] <= heights[r]):
                l = l + 1
            else:
                r = r - 1

        return max