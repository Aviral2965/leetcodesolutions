class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n) % 2 == 0:
            return False

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                previous = set()

                if i > 0:
                    previous |= dp[i - 1][j]

                if j > 0:
                    previous |= dp[i][j - 1]

                change = 1 if grid[i][j] == '(' else -1

                for balance in previous:
                    new_balance = balance + change

                    if new_balance < 0:
                        continue

                    remaining = (m - 1 - i) + (n - 1 - j)

                    if new_balance <= remaining:
                        dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]