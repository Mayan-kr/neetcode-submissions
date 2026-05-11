class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for item in tokens:

            if item == '+':
                top = stack.pop()
                res=int(stack.pop()) + int(top)
                stack.append(res)

            elif item == '-':
                top = stack.pop()
                res=int(stack.pop()) - int(top)
                stack.append(res)

            elif item == '*':
                top = stack.pop()
                res=int(stack.pop()) * int(top)
                stack.append(res)

            elif item == '/':
                top = stack.pop()
                res= int( int(stack.pop()) / int(top))
                stack.append(res)

            else:
                stack.append(int(item))
                 
        return stack.pop()