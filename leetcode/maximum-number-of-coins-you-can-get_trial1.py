class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort()
        index = len(piles) - 2
        total = 0
        for i in range(n):
            total += piles[index]
            index -= 2
        return total    