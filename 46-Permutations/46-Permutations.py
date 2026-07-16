# Last updated: 7/16/2026, 3:57:28 PM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    backtrack(path)

                    path.pop()
                    used[i] = False

        backtrack([])
        return ans