# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        curr = head
        while curr:
            c+=1
            curr = curr.next
        
        if(c%2!=0):
            k = c/2 +.5
            # curr2 = head
            while k>1:
                head = head.next
                k-=1
            return head
        else:
            k = c/2 +1
            while k>1:
                head = head.next
                k-=1
            return head
        