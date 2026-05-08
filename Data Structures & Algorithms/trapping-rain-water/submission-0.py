class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0
            
        prefix_max=[0] * len(height)
        suffix_max=[0] * len(height)
        left_max, right_max = 0 , 0
        max_ar=0

        for i in range(len(height)):
            if height[i] > left_max:
                left_max=height[i]
                prefix_max[i]=left_max
            else:
                prefix_max[i]=left_max


        for i in range(len(height)-1,-1,-1):
            if height[i] > right_max:
                right_max=height[i]
                suffix_max[i]=right_max
            else:
                suffix_max[i]=right_max

        for i in range(len(height)):
            water= max( 0 ,min( prefix_max[i],suffix_max[i] ) - height[i])
            max_ar += water
        return max_ar