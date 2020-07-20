class Node:

    def __init__(self, value, next):
        self.value = value
        self.next = next

    
def print_list(head):
    cur = head
    while(cur != None):
        print(cur.value)
        cur = cur.next


def reverse_list(head):
    trail, cur, trail.next = (head, head.next, None)
    while(cur != None):
        temp = cur
        cur = cur.next
        temp.next = trail
        trail = temp
    return trail

l = Node(1, Node(2, Node(3, Node(4, None))))

r = reverse_list(l)

print_list(r)
