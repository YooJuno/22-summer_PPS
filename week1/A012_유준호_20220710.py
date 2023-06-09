class Solution:
    def countPrimes(self, n: int) -> int:
        t = [True for i in range(n)]
        i = 2
        while i * i < n:
            if t[i] is False:
                i += 1
                continue
            j = i * i
            while j < n:
                t[j] = False
                j += i
            i += 1
        res = 0
        for i in range(2, n):
            if t[i] is True:
                res += 1
        return res 