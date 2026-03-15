class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x, y = 0, 1
        for i in range(len(nums)):
            if nums[y] > nums[x]:
                x += 1
                y += 1
            else:
                y += 1


