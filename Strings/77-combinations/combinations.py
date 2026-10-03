class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res=[]
        def b(s,p):
            if len(p)==k:
                res.append(p[:])
                return
            for i in range(s,n+1):
                p.append(i)
                b(i+1,p)
                p.pop()
        b(1,[])
        return res