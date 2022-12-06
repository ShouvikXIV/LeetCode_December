# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = []
        even = []
        result = []
        c = 1
        curr = head
        while curr:
            if(c%2!=0):
                odd.append(curr.val)
            else:
                even.append(curr.val)
            c+=1
            curr = curr.next
        # print(odd)
        # print(even)
        for i in odd:
            result.append(i)
        for i in even:
            result.append(i)
        
        curr2 = head
        k = 0
        while curr2 and k<len(odd):
            curr2.val = odd[k]
            k+=1
            curr2 = curr2.next
        g = 0
        while curr2 and g<len(even):
            curr2.val = even[g]
            g+=1
            curr2 = curr2.next
        
        return head
        # return result
        # LN = ListNode(result[0])