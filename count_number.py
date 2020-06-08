class Solution:
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        start = 9
        permutes = 9
        digits = n
        while digits > 1 and start:
            permutes *= start
            start -= 1
            digits -= 1
        return permutes + self.countNumbersWithUniqueDigits(n-1)


sol = Solution()
print(sol.countNumbersWithUniqueDigits(2))