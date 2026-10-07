class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res,p=[],[]
        def b(i):
            if len(p)==len(nums):
                res.append(p[:])
                return
            for i in range(len(nums)):
                if nums[i] not in p:
                    p.append(nums[i])
                    b(i+1)
                    p.pop()
            return res
        return b(1)