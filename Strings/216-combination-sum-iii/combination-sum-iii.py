class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res,t=[],[]
        def p(s,rem):
            if len(t)==k and rem==0:
                res.append(t[:])
                return
            for i in range(s,10):
                if sum(t)+i>n:
                    continue
                t.append(i)
                p(i+1,rem-i)
                t.pop()
            return res
        return p(1,n)