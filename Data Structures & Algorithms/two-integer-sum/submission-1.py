class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pocket={}
        for i,num in enumerate(nums):
            find=target-num
            if find in pocket:
                return [pocket[find],i]
            pocket[num]=i