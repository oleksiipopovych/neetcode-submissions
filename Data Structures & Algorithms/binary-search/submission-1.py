class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while (lo < hi):
            m = math.floor((hi - lo) / 2) + lo
            if (nums[m] == target):
                return m
            
            if (nums[m] > target):
                hi = m
            
            if (nums[m] < target):
                lo = m + 1
        
        return -1
        