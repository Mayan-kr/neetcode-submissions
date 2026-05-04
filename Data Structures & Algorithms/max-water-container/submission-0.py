class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        Max_ar=0
        
        while l < r:

            if heights[l] <= heights[r]:
                Area= (r-l) * heights[l]
                if Area > Max_ar:
                    Max_ar=Area
                l += 1

            elif heights[r] < heights[l]:
                Area= (r-l) * heights[r]
                if Area > Max_ar:
                    Max_ar=Area
                r -= 1
        return Max_ar
                
            

        