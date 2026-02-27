class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums.sort()
        for i , v in enumerate(nums):
            if v == target:
                ans.append(i)
        return ans