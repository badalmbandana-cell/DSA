class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        yoyo=set(nums)
        m=len(yoyo)
        if n==m:
            return False
        return True        
        