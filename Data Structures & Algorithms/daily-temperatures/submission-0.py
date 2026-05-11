class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        output=[0]*len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and t > temperatures[ stack[-1] ]:
                stack_idx= stack.pop()
                output[ stack_idx ]= i-stack_idx
            
            stack.append(i)
        
        return output



