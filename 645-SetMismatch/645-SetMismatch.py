# Last updated: 7/16/2026, 3:57:23 PM
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
       n=len(nums)
       sumn=n*(n+1)//2#expected
       sums=sum(nums)#actual
       sumsqn=n*(n+1)*(2*n+1)//6
       actualsqp=sum(i*i for i in nums)
       diff_linear=sumn-sums#expected-actualm-d
       diff_sq=sumsqn-actualsqp#m2-d2
       sum_linear=diff_sq//diff_linear#m+d formula 
       missingnumber=(diff_linear+sum_linear)//2
       duplicate=sum_linear-missingnumber
       return [duplicate,missingnumber]

       