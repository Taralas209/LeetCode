class Solution:
    def countOdds(self, low, high):
        return (high - low + 1 + low % 2 + high % 2) // 2
