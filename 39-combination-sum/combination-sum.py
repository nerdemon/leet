class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def back_track(start,remaining,current):
            if remaining==0:
                result.append(list(current))
                return
            if remaining<0:
                return 
            for i in range(start,len(candidates)):
                current.append(candidates[i])
                back_track(i,remaining-candidates[i],current)
                current.pop()
        back_track(0,target,[])
        return result