class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count={}
        for num in arr:
            count[num]=count.get(num,0)+1
        occurence=set()
        for val in count.values():
            if val in occurence:
                return False
            occurence.add(val)
        return True                     
        