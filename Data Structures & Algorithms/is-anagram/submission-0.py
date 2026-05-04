class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        temp=list(t)
        for i in s:
            if i in temp:
                temp.remove(i)
        if len(temp)==0:
            return True
        else:
            return False    
      
        