class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=set()
        s=set(nums1)
        for val in nums2:
            if val in s:
                result.add(val)
        return list(result)            
