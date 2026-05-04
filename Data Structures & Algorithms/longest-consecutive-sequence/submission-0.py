class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sorted_nums=sorted(list(set(nums)))
        
        longest=1
        count=1

        for i in range(1,len(sorted_nums)):
            if sorted_nums[i]==sorted_nums[i-1]+1:
                count+=1
            else:
                count=1
            longest=max(longest,count)

        return longest