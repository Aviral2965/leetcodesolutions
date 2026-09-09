class Solution:
    def countCommas(self, n):
        ans = 0
        start = 1000

        while start <= n:
            end = min(n, start * 1000 - 1)

            commas = (len(str(start)) - 1) // 3

            ans += (end - start + 1) * commas

            start *= 1000

        return ans