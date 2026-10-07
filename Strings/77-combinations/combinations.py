class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res,p=[],[]
        def b(i):
            if len(p)==k:
                res.append(p[:])
                return
            for i in range(i,n+1):
                p.append(i)
                b(i+1)
                p.pop()
            return res
        return b(1)