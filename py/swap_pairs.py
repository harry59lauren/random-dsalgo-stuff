
class NULL:
    def is_null(self):
        return True

class ListNode:

    def __init__(self, val, next):
        self.val = val
        self.next = next
    
    def is_null(self):
        return False




l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, NULL())))))



def swap_adjacent_nodes(linked_list):

    if linked_list.is_null() or linked_list.next.is_null():
        return linked_list
    
    current_pair = linked_list
    first = linked_list.next

    while True:
        next_pair = current_pair.next.next
        current_pair.next.next = current_pair
        current_pairii




swapped = swap_adjacent_nodes(l)

cur = swapped

while not cur.is_null():
    print(cur.val)
    cur = cur.next