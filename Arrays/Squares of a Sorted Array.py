class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        dp=[]
        for i in nums:
            dp.append(i**2)
            dp.sort()
        return dp