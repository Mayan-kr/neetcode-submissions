class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        
        for item in tokens:
            if item == "+":
                stack.append(stack.pop() + stack.pop())
            elif item == "-":
                top = stack.pop()
                stack.append(stack.pop() - top)
            elif item == "*":
                stack.append(stack.pop() * stack.pop())
            elif item == "/":
                top = stack.pop()
                bottom = stack.pop()
                # Use int(a / b) for truncation toward zero
                stack.append(int(bottom / top))
            else:
                # CAST HERE to avoid the TypeError at the end
                stack.append(int(item))
                 
        return stack.pop()