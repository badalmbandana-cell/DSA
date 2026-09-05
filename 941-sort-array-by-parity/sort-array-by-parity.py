class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        new=sorted(nums)
        result1=[]
        result2=[]
        for val in new:
            if val%2==0:
                result1.append(val)
            else:
                result2.append(val)
        result=result1+result2
        return result           


        