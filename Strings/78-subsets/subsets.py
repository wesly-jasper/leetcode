class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res,p=[],[]
        def b(i):
            res.append(p[:])
            for i in range(i,len(nums)):
                p.append(nums[i])
                b(i+1)
                p.pop()
            return res
        return b(0)