class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence
        for i in range(n):
            c = ord(s[i]) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Find valid substrings
        for i in range(n):

            c = ord(s[i]) - ord('a')

            if i != first[c]:
                continue

            l = i
            r = last[c]
            j = l
            valid = True

            while j <= r:

                x = ord(s[j]) - ord('a')

                if first[x] < l:
                    valid = False
                    break

                r = max(r, last[x])
                j += 1

            if valid:
                intervals.append((l, r))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for l, r in intervals:

            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans