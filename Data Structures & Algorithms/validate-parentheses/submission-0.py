class Solution:
    def isValid(self, s: str) -> bool:
        map= {")": "(", "}": "{", "]": "["}
        stack=[]

        for symbol in s:
            if symbol in map:
                if stack and stack[-1] == map[symbol]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(symbol)
        return True if not stack else False