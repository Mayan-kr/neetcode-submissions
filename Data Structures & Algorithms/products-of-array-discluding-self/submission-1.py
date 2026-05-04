class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total_product = 1
        
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num
                
        if zero_count > 1:
            return [0] * len(nums)
            
        elif zero_count == 1:
            return [total_product if num == 0 else 0 for num in nums]
            
        else:
            return [total_product // num for num in nums]