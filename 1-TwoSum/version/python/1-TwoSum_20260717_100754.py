# Last updated: 7/17/2026, 10:07:54 AM
# hashmap
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        mp = {}
4
5        for i in range(len(nums)):
6            need = target - nums[i]
7
8            if need in mp:
9                return [mp[need], i]
10
11            mp[nums[i]] = i