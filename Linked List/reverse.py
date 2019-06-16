def reverseListIterative(head):

    if not head:
        return

    prev = None
    cur = head
    print cur
    while cur:

        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    return prev
    
    
    
def reverseListRecursive(self, head):
    if not head or not head.next:
        return head

    new_head = self.reverseListRecursive(head.next)
    next_node = head.next    #        head -> next_node 
    next_node.next = head    #        head <- next_node 
    head.next = None         #        [x] <- head <- next_node 
    return new_head
