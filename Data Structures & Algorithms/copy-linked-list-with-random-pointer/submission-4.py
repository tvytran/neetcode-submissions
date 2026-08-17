"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        store = {}

        another = head 

        while another:
            copy = Node(another.val)
            store[another] = copy

            another = another.next
        
        for old, new in store.items():
            if old.next:
                new.next = store[old.next]
            
            if old.random:
                new.random = store[old.random]
            
        return store[head]
        