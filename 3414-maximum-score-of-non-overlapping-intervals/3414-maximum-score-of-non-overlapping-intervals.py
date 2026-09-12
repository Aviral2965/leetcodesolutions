from bisect import bisect_left


class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Store: (left, right, weight, original_index)
        arr = []

        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort intervals by ending position
        arr.sort(key=lambda x: x[1])

        ends = [x[1] for x in arr]

        # dp_score[i][k] = maximum score using first i intervals
        # choosing exactly k intervals
        dp_score = [[0] * 5 for _ in range(n + 1)]

        # dp_indices[i][k] = lexicographically smallest
        # indices giving that maximum score
        dp_indices = [[()] * 5 for _ in range(n + 1)]

        for i in range(1, n + 1):

            l, r, w, original_index = arr[i - 1]

            # Previous interval must end strictly before l
            p = bisect_left(ends, l, 0, i - 1)

            # Option 1: Skip current interval
            for k in range(5):
                dp_score[i][k] = dp_score[i - 1][k]
                dp_indices[i][k] = dp_indices[i - 1][k]

            # Option 2: Take current interval
            for k in range(1, 5):

                candidate_score = dp_score[p][k - 1] + w

                candidate_indices = tuple(
                    sorted(
                        dp_indices[p][k - 1] + (original_index,)
                    )
                )

                if candidate_score > dp_score[i][k]:
                    dp_score[i][k] = candidate_score
                    dp_indices[i][k] = candidate_indices

                elif candidate_score == dp_score[i][k]:
                    if candidate_indices < dp_indices[i][k]:
                        dp_indices[i][k] = candidate_indices

        # Choose the best score using at most 4 intervals
        best_score = -1
        answer = ()

        for k in range(5):
            if dp_score[n][k] > best_score:
                best_score = dp_score[n][k]
                answer = dp_indices[n][k]

            elif dp_score[n][k] == best_score:
                if dp_indices[n][k] < answer:
                    answer = dp_indices[n][k]

        return list(answer)