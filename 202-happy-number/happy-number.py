class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True  
        visited=set()
        while n!=1 and n not in visited:
            visited.add(n)
            summ=0
            while n>0:
                rem=n%10
                summ=summ+rem*rem
                n=n//10
            n=summ 
        return n==1          

                 
        