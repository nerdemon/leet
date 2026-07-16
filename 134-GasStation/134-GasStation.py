# Last updated: 7/16/2026, 3:57:20 PM
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        start,current_tank=0,0
        for i in range(len(gas)):
            current_tank+=gas[i]-cost[i]
            if current_tank<0:
                start=i+1
                current_tank=0
        return start