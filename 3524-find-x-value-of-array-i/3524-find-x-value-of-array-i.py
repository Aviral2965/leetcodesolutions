class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        result = [0] * k

        n = len(nums)

        for i in range(n):
            product = 1

            for j in range(i, n):
                product = (product * nums[j]) % k
                result[product] += 1

        return result