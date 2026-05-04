class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pocket=set()
        for i in nums:
            if i in pocket:
                return True
            pocket.add(i)
        return False
