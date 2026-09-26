class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroes = 0;
        for n in nums:
            if n != 0:
                product = product * n;
            else:
                zeroes += 1

        for (i, n) in enumerate(nums):
            if zeroes > 1 or n != 0 and zeroes == 1:
                nums[i] = 0;

            if n == 0 and zeroes == 1:
                nums[i] = product


            if n != 0 and zeroes == 0:
                nums[i] = int(product / n)
                

        return nums