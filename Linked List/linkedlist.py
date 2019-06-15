

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self,val):

        if not self.head:
            self.head = Node(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)


    def printList(self):
        if not self.head:
            print None

        else:
            cur = self.head
            while(cur):
                print cur.val
                cur = cur.next


    def delete(self,val):
        if not self.head:
            return None

        cur = self.head

        while cur:
            prev = cur
            cur = cur.next

            if cur.val == val:
                prev.next = cur.next




def swapValues(head):


    a = head
    b = head.next
    c = head.next.next

    a.next = c
    b.next = a


    cur = a

    while cur and cur.next:

        first = cur
        second = cur.next
        third = cur.next.next

        if not third:
            break

        first.next = third
        second.next = third.next
        third.next = second

        cur = second


    return b


def printList(head):
    if not head:
        print None

    else:
        cur = head
        while(cur):
            print cur.val
            cur = cur.next



l = LinkedList()
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.add(6)
l.add(7)


#l.printList()

x = swapValues(l.head)



printList(x)











