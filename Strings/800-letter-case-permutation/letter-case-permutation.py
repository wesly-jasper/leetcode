class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        t=[]
        res=[]
        def p(i):
            if i==len(s):
                res.append("".join(t))
                return
            ch=s[i]
            if ch.isalpha():
                for c in (ch.lower(),ch.upper()):
                    t.append(c)
                    p(i+1)
                    t.pop()
            else:
                t.append(ch)
                p(i+1)
                t.pop()
            return res
        return p(0)