class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        if nums.count(0) > 1:
            return [0] * len(nums)

        elif nums.count(0) == 1:
            mul=1
            for num in nums:
                if num==0:
                    output.append(0)
                    continue
                mul *=num
                output.append(0)
            output[nums.index(0)]=mul
            return output

        else:
            mul=1
            for num in nums:
                mul*=num
    
            for num in nums:
                output.append(int(mul/num))
            return output
                

                

        
        

