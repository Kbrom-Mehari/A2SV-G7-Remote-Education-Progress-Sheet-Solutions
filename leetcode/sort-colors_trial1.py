class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maxx = max(nums)
        count = [0] * (maxx + 1)
        for num in nums:
            count[num] += 1
        index = 0
        for i , v in enumerate(count):
            while v > 0:
                nums[index] = i
                index += 1
                v -= 1
            

