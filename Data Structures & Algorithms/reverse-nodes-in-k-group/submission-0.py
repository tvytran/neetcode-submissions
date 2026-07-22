# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cl = head
        length = 0
        while cl:
            length +=1
            cl = cl.next
        loop = length//k
        newh = head

        p = head.next
        q = head
        r = head.next
        end = ListNode()
        for i in range(loop):
            p = None
            hold = q
            for j in range(k):
                if i == 0 and j == k-1:
                    newh = q
                q.next = p
                p = q
                q = r
                if r:
                    r= r.next
            end.next = p
            end = hold
        if length%k != 0:
            end.next = q


        return newh
        