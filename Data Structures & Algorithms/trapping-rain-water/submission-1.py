class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0
            
        n = len(height)
        # 1. Initialize lists with size n
        prefix_max = [0] * n
        suffix_max = [0] * n
        left_max, right_max = 0, 0
        max_ar = 0

        # 2. Fill prefix_max
        for i in range(n):
            left_max = max(left_max, height[i])
            prefix_max[i] = left_max

        # 3. Fill suffix_max (Iterating backwards)
        for i in range(n - 1, -1, -1):
            right_max = max(right_max, height[i])
            suffix_max[i] = right_max

        # 4. Calculate total water
        for i in range(n):
            max_ar += max(0, min(prefix_max[i], suffix_max[i]) - height[i])
            
        return max_ar