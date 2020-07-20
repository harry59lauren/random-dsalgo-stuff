from global_structures import ListNode

def print_list(head):
    cur = head
    while(cur):
        print(cur.value)
        cur = cur.next

def rotate_right_by_k(l, k):
    '''
    Rotates a linked list to the right k spaces
    '''
    anchor = l
    cur = l
    steps = k - 1

    if(steps < 0):
        return anchor

    while steps:
        cur = cur.next
        if not cur:
            cur = anchor
        steps = steps - 1
    
    tail = cur

    while tail.next:
        tail = tail.next

    tail.next = anchor
    anchor = cur.next
    cur.next = None

    return anchor



   



l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))

n = rotate_right_by_k(l, 100000000)

print(n)

