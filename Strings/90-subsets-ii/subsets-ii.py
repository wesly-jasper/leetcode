class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res,t=[],[]
        def p(i):
            if i==len(nums):
                if t not in res:
                    res.append(t[:])
                return
            t.append(nums[i])
            p(i+1)
            t.pop()
            p(i+1)
            return sorted(res)
        return p(0)