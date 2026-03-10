class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        x = 0
        y = 0
        for i in range(len(nums)):            
            if nums[i] == 0:
                x = i