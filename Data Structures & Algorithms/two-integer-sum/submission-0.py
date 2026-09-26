class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            neededNum = target - num
            if neededNum in seen:
                return [seen[neededNum], index]
            seen[num] = index

        