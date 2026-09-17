# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy=ListNode(0)
        dummy.next=head
        curr=dummy
        count=0
        while curr!=None:
            count+=1
            curr=curr.next   
        curr=dummy
        for i in range(count-n-1):
            curr=curr.next
        curr.next=curr.next.next
        return dummy.next   
        