# Last updated: 7/17/2026, 10:16:35 AM
# backtracking
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        result=[]
4        def back_track(start,remaining,current):
5            if remaining==0:
6                result.append(list(current))
7                return
8            if remaining<0:
9                return 
10            for i in range(start,len(candidates)):
11                current.append(candidates[i])
12                back_track(i,remaining-candidates[i],current)
13                current.pop()
14        back_track(0,target,[])
15        return result