class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for r in nums:
            g=str(r)
            if len(g)%2==0:
                count+=1
        return count