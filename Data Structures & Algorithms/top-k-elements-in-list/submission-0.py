class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # 2. Get a list of all the unique numbers
        unique_nums = list(count.keys())
        
        # 3. Sort the unique numbers based on their frequency (descending)
        unique_nums.sort(key=lambda x: count[x], reverse=True)
        
        # 4. Return the first k elements
        return unique_nums[:k]

        